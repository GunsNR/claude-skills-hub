"""Cost-optimized model routing for OpenRouter.

Policy lives in config/openrouter_routing.json: each route class maps to a
primary model and cheaper fallbacks, with per-million-token cost estimates
and a daily budget cap. When today's estimated spend crosses the soft cap,
every route class downgrades to its cheapest model; the hard cap forces
free-tier models only.

This is the "save the most on AI costs" layer: most CEO-layer traffic
(classification, summaries, daily logs) never needs a frontier model.
"""

import json
from datetime import datetime, time, timezone
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import ModelUsage

DEFAULT_CONFIG = {
    "daily_budget_usd": 2.00,
    "hard_cap_usd": 5.00,
    "routes": {
        "fast": {"models": ["google/gemini-2.5-flash-lite", "deepseek/deepseek-chat-v3.1:free"]},
        "summarization": {"models": ["google/gemini-2.5-flash-lite", "deepseek/deepseek-chat-v3.1:free"]},
        "classification": {"models": ["deepseek/deepseek-chat-v3.1:free", "google/gemini-2.5-flash-lite"]},
        "growth": {"models": ["anthropic/claude-sonnet-4.6", "google/gemini-2.5-flash"]},
        "reasoning": {"models": ["anthropic/claude-opus-4.8", "anthropic/claude-sonnet-4.6"]},
        "coding": {"models": ["anthropic/claude-sonnet-4.6", "deepseek/deepseek-chat-v3.1:free"]},
        "research": {"models": ["anthropic/claude-sonnet-4.6", "google/gemini-2.5-flash"]},
    },
    "cost_per_mtok_usd": {
        "deepseek/deepseek-chat-v3.1:free": 0.0,
        "google/gemini-2.5-flash-lite": 0.30,
        "google/gemini-2.5-flash": 1.25,
        "anthropic/claude-sonnet-4.6": 9.0,
        "anthropic/claude-opus-4.8": 35.0,
    },
    "free_fallback": "deepseek/deepseek-chat-v3.1:free",
}


class CostRouter:
    def __init__(self, db: Session, config: dict | None = None,
                 config_path: str | Path | None = None):
        self.db = db
        if config is None and config_path is not None:
            config = json.loads(Path(config_path).read_text(encoding="utf-8"))
        self.config = config or DEFAULT_CONFIG

    def spend_today(self) -> float:
        start = datetime.combine(
            datetime.now(timezone.utc).date(), time.min, tzinfo=timezone.utc)
        rows = self.db.scalars(
            select(ModelUsage).where(ModelUsage.created_at >= start))
        return round(sum(r.est_cost for r in rows), 6)

    def choose_model(self, route_class: str) -> str:
        routes = self.config["routes"]
        route = routes.get(route_class) or routes.get("fast")
        models = route["models"]
        spent = self.spend_today()
        if spent >= self.config["hard_cap_usd"]:
            return self.config["free_fallback"]
        if spent >= self.config["daily_budget_usd"]:
            # soft cap: cheapest model configured for this route
            costs = self.config["cost_per_mtok_usd"]
            return min(models, key=lambda m: costs.get(m, 999))
        return models[0]

    def estimate_cost(self, model: str, tokens: int) -> float:
        per_mtok = self.config["cost_per_mtok_usd"].get(model, 5.0)
        return round(tokens / 1_000_000 * per_mtok, 6)

    def record_usage(self, route_class: str, model: str, tokens: int,
                     est_cost: float) -> None:
        self.db.add(ModelUsage(route_class=route_class, model=model,
                               tokens=tokens, est_cost=est_cost))
        self.db.commit()

    def usage_summary(self) -> dict:
        spent = self.spend_today()
        return {
            "spend_today_usd": spent,
            "daily_budget_usd": self.config["daily_budget_usd"],
            "hard_cap_usd": self.config["hard_cap_usd"],
            "budget_remaining_usd": round(
                max(self.config["daily_budget_usd"] - spent, 0), 6),
            "downgraded": spent >= self.config["daily_budget_usd"],
        }
