"""Database session management.

Standalone mode uses its own SQLite file (SMARTOS_CEO_DB env var, defaults
to ./smartos_ceo.db). When integrated into Smart OS, call configure() with
the host app's engine instead so everything lives in one database.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


_engine = None
_SessionLocal = None


def configure(engine=None, db_url: str | None = None) -> None:
    """Bind the CEO layer to an engine (host app) or a URL (standalone)."""
    global _engine, _SessionLocal
    if engine is None:
        url = db_url or os.environ.get(
            "SMARTOS_CEO_DB", "sqlite:///smartos_ceo.db"
        )
        engine = create_engine(url, connect_args={"check_same_thread": False}
                               if url.startswith("sqlite") else {})
    _engine = engine
    _SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    Base.metadata.create_all(engine)


def get_session() -> Session:
    if _SessionLocal is None:
        configure()
    return _SessionLocal()


def get_db():
    """FastAPI dependency."""
    db = get_session()
    try:
        yield db
    finally:
        db.close()
