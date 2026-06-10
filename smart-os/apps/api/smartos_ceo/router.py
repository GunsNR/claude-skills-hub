"""FastAPI router for the CEO layer. Mounts at /api/ceo."""

from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from . import (auto_research, business, ceo_brief, notify, obsidian, studio,
               tasks, tax_guard, wiki)
from .cost_router import CostRouter
from .db import get_db
from .gateway import build_gateway

router = APIRouter(prefix="/api/ceo", tags=["ceo"])
STATIC_DIR = Path(__file__).parent / "static"


# ---------- schemas ----------

class CaptureIn(BaseModel):
    text: str = Field(min_length=1, max_length=2000)
    client_id: int | None = None


class SnoozeIn(BaseModel):
    hours: int = Field(default=24, ge=1, le=24 * 30)


class DoneIn(BaseModel):
    learning: str | None = None


class OwnerIn(BaseModel):
    owner: str = Field(pattern="^(izzy|dilshan)$")


class ClientIn(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    domain: str = ""
    mrr: float = 0.0
    status: str = "active"
    notes: str = ""


class LogIn(BaseModel):
    entry: str = Field(min_length=1, max_length=2000)
    kind: str = "note"


class DelegateIn(BaseModel):
    title: str = Field(min_length=1, max_length=500)
    details: str = ""
    client_id: int | None = None


class IncomeIn(BaseModel):
    amount: float = Field(gt=0)
    description: str = ""
    client_id: int | None = None


class TaxRateIn(BaseModel):
    rate: float = Field(gt=0, lt=1)


class NoteIn(BaseModel):
    rel_path: str = Field(min_length=1, max_length=300)
    content: str


class LogEntryIn(BaseModel):
    entry: str = Field(min_length=1, max_length=2000)


class LearningIn(BaseModel):
    text: str = Field(min_length=1, max_length=2000)
    source_task_id: int | None = None


class ResearchIn(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    context: str = ""


def _task_out(t) -> dict:
    return {"id": t.id, "title": t.title, "owner": t.owner,
            "category": t.category, "impact": t.impact, "urgency": t.urgency,
            "minutes": t.minutes, "status": t.status}


# ---------- brief + tasks ----------

@router.get("/brief")
def get_brief(db: Session = Depends(get_db)):
    return ceo_brief.build(db)


@router.post("/capture")
def capture_task(body: CaptureIn, db: Session = Depends(get_db)):
    task = tasks.capture(db, body.text, client_id=body.client_id)
    return _task_out(task)


@router.get("/tasks")
def list_tasks(owner: str | None = None, db: Session = Depends(get_db)):
    return [_task_out(t) for t in tasks.open_tasks(db, owner=owner)]


@router.post("/tasks/{task_id}/done")
def complete_task(task_id: int, body: DoneIn = DoneIn(),
                  db: Session = Depends(get_db)):
    task = tasks.complete(db, task_id)
    if task is None:
        raise HTTPException(404, "task not found")
    if body.learning:
        wiki.add_learning(db, task.category, body.learning,
                          source_task_id=task.id)
    return _task_out(task)


@router.post("/tasks/{task_id}/snooze")
def snooze_task(task_id: int, body: SnoozeIn = SnoozeIn(),
                db: Session = Depends(get_db)):
    task = tasks.snooze(db, task_id, hours=body.hours)
    if task is None:
        raise HTTPException(404, "task not found")
    return _task_out(task)


@router.post("/tasks/{task_id}/owner")
def reassign_task(task_id: int, body: OwnerIn, db: Session = Depends(get_db)):
    task = tasks.set_owner(db, task_id, body.owner)
    if task is None:
        raise HTTPException(404, "task not found")
    out = _task_out(task)
    if body.owner == "dilshan":
        out["notified"] = notify.notify_dilshan(task.title, task.details)
    return out


# ---------- clients + delegation ----------

@router.post("/clients")
def create_client(body: ClientIn, db: Session = Depends(get_db)):
    c = business.create_client(db, body.name, body.domain, body.mrr,
                               body.status, body.notes)
    return {"id": c.id, "name": c.name}


@router.get("/clients")
def list_clients(db: Session = Depends(get_db)):
    return business.client_health(db)


@router.post("/clients/{client_id}/log")
def log_client(client_id: int, body: LogIn, db: Session = Depends(get_db)):
    log = business.log_interaction(db, client_id, body.entry, body.kind)
    if log is None:
        raise HTTPException(404, "client not found")
    return {"id": log.id, "client_id": client_id}


@router.post("/delegate")
def delegate(body: DelegateIn, db: Session = Depends(get_db)):
    return business.delegate(db, body.title, body.details, body.client_id)


@router.get("/delegate/queue")
def delegation_queue(db: Session = Depends(get_db)):
    return [_task_out(t) for t in business.delegation_queue(db)]


# ---------- tax ----------

@router.post("/income")
def record_income(body: IncomeIn, db: Session = Depends(get_db)):
    e = tax_guard.record_income(db, body.amount, body.description,
                                body.client_id)
    return {"id": e.id, "amount": e.amount, "tax_set_aside": e.tax_set_aside}


@router.get("/tax/status")
def tax_status(db: Session = Depends(get_db)):
    return tax_guard.status(db)


@router.post("/tax/sweep")
def tax_sweep(db: Session = Depends(get_db)):
    return tax_guard.sweep(db)


@router.post("/tax/rate")
def set_tax_rate(body: TaxRateIn, db: Session = Depends(get_db)):
    return {"tax_rate": tax_guard.set_rate(db, body.rate)}


# ---------- obsidian ----------

@router.get("/obsidian/index")
def obsidian_index():
    try:
        return obsidian.index_vault()
    except FileNotFoundError as exc:
        raise HTTPException(400, str(exc))


@router.post("/obsidian/note")
def obsidian_note(body: NoteIn):
    try:
        path = obsidian.write_note(body.rel_path, body.content)
    except FileNotFoundError as exc:
        raise HTTPException(400, str(exc))
    except PermissionError as exc:
        raise HTTPException(403, str(exc))
    return {"written": path}


@router.post("/obsidian/daily-log")
def obsidian_daily_log(body: LogEntryIn):
    try:
        path = obsidian.append_daily_log(body.entry)
    except FileNotFoundError as exc:
        raise HTTPException(400, str(exc))
    return {"written": path}


# ---------- wiki ----------

@router.get("/wiki")
def wiki_list(db: Session = Depends(get_db)):
    return [{"category": p.category, "updated_at": p.updated_at.isoformat()}
            for p in wiki.list_pages(db)]


@router.get("/wiki/{category}")
def wiki_page(category: str, db: Session = Depends(get_db)):
    page = wiki.get_page(db, category)
    return {"category": page.category, "content": page.content}


@router.post("/wiki/{category}/learning")
def wiki_learning(category: str, body: LearningIn,
                  db: Session = Depends(get_db)):
    learning = wiki.add_learning(db, category, body.text, body.source_task_id)
    return {"id": learning.id, "category": category}


@router.post("/wiki/{category}/distill")
def wiki_distill(category: str, db: Session = Depends(get_db)):
    cr = CostRouter(db)
    page = wiki.distill(db, category, build_gateway(cr), cr)
    return {"category": page.category, "content": page.content}


# ---------- research ----------

@router.post("/research")
def research_enqueue(body: ResearchIn, db: Session = Depends(get_db)):
    item = auto_research.enqueue(db, body.question, body.context)
    return {"id": item.id, "status": item.status}


@router.get("/research")
def research_list(status: str | None = None, db: Session = Depends(get_db)):
    return [{"id": i.id, "question": i.question, "status": i.status,
             "model_used": i.model_used, "brief": i.brief}
            for i in auto_research.list_items(db, status)]


@router.post("/research/{item_id}/run")
def research_run(item_id: int, db: Session = Depends(get_db)):
    cr = CostRouter(db)
    item = auto_research.run(db, item_id, build_gateway(cr), cr)
    if item is None:
        raise HTTPException(404, "research item not found")
    return {"id": item.id, "status": item.status, "brief": item.brief,
            "model_used": item.model_used}


# ---------- studio ----------

class StudioRunIn(BaseModel):
    action_id: str = Field(min_length=1, max_length=100)
    input: str = Field(min_length=1, max_length=20000)


def _job_out(j) -> dict:
    return {"id": j.id, "action_id": j.action_id, "label": j.label,
            "output_kind": j.output_kind, "output_text": j.output_text,
            "file_name": j.file_name, "model_used": j.model_used,
            "est_cost": j.est_cost, "status": j.status,
            "created_at": j.created_at.isoformat(),
            "input_preview": j.input_text[:120]}


@router.get("/studio/actions")
def studio_actions():
    return studio.list_actions()


@router.post("/studio/run")
def studio_run(body: StudioRunIn, db: Session = Depends(get_db)):
    cr = CostRouter(db)
    job = studio.run(db, body.action_id, body.input, build_gateway(cr), cr)
    if job is None:
        raise HTTPException(404, "unknown action")
    return _job_out(job)


@router.get("/studio/jobs")
def studio_jobs(limit: int = 30, db: Session = Depends(get_db)):
    return [_job_out(j) for j in studio.history(db, limit)]


@router.get("/studio/files/{job_id}/{file_name}")
def studio_file(job_id: int, file_name: str):
    try:
        return FileResponse(studio.get_file(job_id, file_name))
    except FileNotFoundError:
        raise HTTPException(404, "file not found")


@router.get("/studio", include_in_schema=False)
def studio_page():
    return FileResponse(STATIC_DIR / "studio.html")


# ---------- model spend ----------

@router.get("/usage")
def usage(db: Session = Depends(get_db)):
    return CostRouter(db).usage_summary()


# ---------- dashboard ----------

@router.get("/dashboard", include_in_schema=False)
def dashboard():
    return FileResponse(STATIC_DIR / "dashboard.html")


@router.get("/manifest.json", include_in_schema=False)
def manifest():
    return FileResponse(STATIC_DIR / "manifest.json")
