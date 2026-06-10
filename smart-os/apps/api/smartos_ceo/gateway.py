"""Model gateway.

Standalone mode talks to OpenRouter directly using OPENROUTER_API_KEY from
the environment (never persisted, never logged, never returned to clients).
With no key configured it falls back to a deterministic mock so the whole
system stays usable and testable offline.

When integrated into Smart OS, replace this with an adapter over the host
app's model gateway — the interface is one method: generate().
"""

import os

import httpx

from .cost_router import CostRouter

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class MockGateway:
    """Deterministic offline gateway. Default when no API key is set."""

    def generate(self, route_class: str, prompt: str, system: str = "") -> dict:
        return {
            "text": f"[mock:{route_class}] " + prompt[:200],
            "model": "mock",
            "tokens": len(prompt) // 4,
            "est_cost": 0.0,
        }


class OpenRouterGateway:
    def __init__(self, cost_router: CostRouter, api_key: str | None = None,
                 timeout: float = 60.0):
        self._key = api_key or os.environ.get("OPENROUTER_API_KEY", "")
        self.cost_router = cost_router
        self.timeout = timeout

    @property
    def available(self) -> bool:
        return bool(self._key)

    def generate(self, route_class: str, prompt: str, system: str = "") -> dict:
        model = self.cost_router.choose_model(route_class)
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        resp = httpx.post(
            OPENROUTER_URL,
            headers={"Authorization": f"Bearer {self._key}"},
            json={"model": model, "messages": messages},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        text = data["choices"][0]["message"]["content"]
        usage = data.get("usage", {})
        tokens = usage.get("total_tokens", len(prompt) // 4)
        est_cost = self.cost_router.estimate_cost(model, tokens)
        return {"text": text, "model": model, "tokens": tokens,
                "est_cost": est_cost}


def build_gateway(cost_router: CostRouter):
    gw = OpenRouterGateway(cost_router)
    return gw if gw.available else MockGateway()
