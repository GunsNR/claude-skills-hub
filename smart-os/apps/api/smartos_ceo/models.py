"""SQLAlchemy models for the CEO layer."""

from datetime import datetime, timezone

from sqlalchemy import (JSON, Boolean, DateTime, Float, ForeignKey, Integer,
                        String, Text)
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Task(Base):
    __tablename__ = "ceo_tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(500))
    details: Mapped[str] = mapped_column(Text, default="")
    owner: Mapped[str] = mapped_column(String(50), default="izzy")  # izzy | dilshan
    category: Mapped[str] = mapped_column(String(50), default="admin")
    # impact/urgency: 1 (low) .. 3 (high)
    impact: Mapped[int] = mapped_column(Integer, default=2)
    urgency: Mapped[int] = mapped_column(Integer, default=2)
    energy: Mapped[str] = mapped_column(String(20), default="medium")  # low|medium|high
    minutes: Mapped[int] = mapped_column(Integer, default=30)
    status: Mapped[str] = mapped_column(String(20), default="open")  # open|done|snoozed
    snoozed_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    client_id: Mapped[int | None] = mapped_column(ForeignKey("ceo_clients.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class Client(Base):
    __tablename__ = "ceo_clients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    domain: Mapped[str] = mapped_column(String(200), default="")
    mrr: Mapped[float] = mapped_column(Float, default=0.0)
    status: Mapped[str] = mapped_column(String(20), default="active")  # active|paused|churned|lead
    notes: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class ClientLog(Base):
    __tablename__ = "ceo_client_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("ceo_clients.id"))
    entry: Mapped[str] = mapped_column(Text)
    kind: Mapped[str] = mapped_column(String(30), default="note")  # note|call|email|deliverable|payment
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class IncomeEvent(Base):
    __tablename__ = "ceo_income_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int | None] = mapped_column(ForeignKey("ceo_clients.id"), nullable=True)
    amount: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String(500), default="")
    tax_set_aside: Mapped[float] = mapped_column(Float, default=0.0)
    swept: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class Setting(Base):
    __tablename__ = "ceo_settings"

    key: Mapped[str] = mapped_column(String(100), primary_key=True)
    value: Mapped[str] = mapped_column(String(500))


class WikiPage(Base):
    __tablename__ = "ceo_wiki_pages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(String(100), unique=True)
    content: Mapped[str] = mapped_column(Text, default="")
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class Learning(Base):
    __tablename__ = "ceo_learnings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(Text)
    source_task_id: Mapped[int | None] = mapped_column(ForeignKey("ceo_tasks.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class ResearchItem(Base):
    __tablename__ = "ceo_research_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    question: Mapped[str] = mapped_column(Text)
    context: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(20), default="queued")  # queued|done|failed
    brief: Mapped[str] = mapped_column(Text, default="")
    model_used: Mapped[str] = mapped_column(String(200), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class ModelUsage(Base):
    __tablename__ = "ceo_model_usage"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    route_class: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(200))
    tokens: Mapped[int] = mapped_column(Integer, default=0)
    est_cost: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class StudioJob(Base):
    __tablename__ = "ceo_studio_jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    action_id: Mapped[str] = mapped_column(String(100))
    label: Mapped[str] = mapped_column(String(200))
    input_text: Mapped[str] = mapped_column(Text)
    output_kind: Mapped[str] = mapped_column(String(20))  # markdown|html|svg
    output_text: Mapped[str] = mapped_column(Text, default="")
    file_name: Mapped[str] = mapped_column(String(200), default="")
    model_used: Mapped[str] = mapped_column(String(200), default="")
    tokens: Mapped[int] = mapped_column(Integer, default=0)
    est_cost: Mapped[float] = mapped_column(Float, default=0.0)
    status: Mapped[str] = mapped_column(String(20), default="done")  # done|failed
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)


class PendingAction(Base):
    __tablename__ = "ceo_pending_actions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    action_type: Mapped[str] = mapped_column(String(100))
    payload: Mapped[dict] = mapped_column(JSON, default=dict)
    risk: Mapped[str] = mapped_column(String(20), default="medium")
    status: Mapped[str] = mapped_column(String(20), default="pending")  # pending|approved|rejected|applied
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    resolved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
