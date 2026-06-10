"""Seed the CEO layer from a business profile YAML.

Usage: python -m smartos_ceo.seed config/rank_logic_seed.yaml

Idempotent: existing clients (matched by name) are updated, not duplicated.
"""

import sys
from pathlib import Path

import yaml
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import tax_guard
from .db import get_session
from .models import Client, Setting


def apply_seed(db: Session, data: dict) -> dict:
    business = data.get("business", {})
    if "tax_rate" in business:
        tax_guard.set_rate(db, float(business["tax_rate"]))
    for key in ("name", "owner"):
        if key in business:
            row = db.get(Setting, f"business_{key}")
            if row is None:
                db.add(Setting(key=f"business_{key}", value=str(business[key])))
            else:
                row.value = str(business[key])

    created, updated = 0, 0
    for spec in data.get("clients", []):
        existing = db.scalar(select(Client).where(Client.name == spec["name"]))
        if existing is None:
            db.add(Client(name=spec["name"], domain=spec.get("domain", ""),
                          mrr=float(spec.get("mrr", 0)),
                          status=spec.get("status", "active"),
                          notes=spec.get("notes", "")))
            created += 1
        else:
            existing.domain = spec.get("domain", existing.domain)
            existing.mrr = float(spec.get("mrr", existing.mrr))
            existing.status = spec.get("status", existing.status)
            updated += 1
    db.commit()
    return {"clients_created": created, "clients_updated": updated,
            "tax_rate": tax_guard.get_rate(db)}


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python -m smartos_ceo.seed <seed.yaml>")
        raise SystemExit(2)
    data = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
    db = get_session()
    try:
        result = apply_seed(db, data)
    finally:
        db.close()
    print(result)


if __name__ == "__main__":
    main()
