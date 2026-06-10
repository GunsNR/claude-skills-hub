import sys
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from smartos_ceo import db as ceo_db  # noqa: E402
from smartos_ceo import obsidian  # noqa: E402


@pytest.fixture()
def db():
    engine = create_engine("sqlite://",
                           connect_args={"check_same_thread": False},
                           poolclass=StaticPool)
    ceo_db.configure(engine=engine)
    session = ceo_db.get_session()
    yield session
    session.close()


@pytest.fixture()
def vault(tmp_path):
    (tmp_path / "Clients").mkdir()
    (tmp_path / "Clients" / "Acme.md").write_text(
        "---\ntitle: Acme Plumbing\nstatus: active\n---\n# Acme\n#client #plumbing\n",
        encoding="utf-8")
    obsidian.configure_vault(str(tmp_path))
    yield tmp_path
    obsidian.configure_vault(None)
