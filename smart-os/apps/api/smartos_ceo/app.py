"""Standalone FastAPI app for the CEO layer.

Inside the full Smart OS backend you do NOT use this file — you mount
`router` into the existing app instead (see docs/INTEGRATION_GUIDE.md).
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .db import configure
from .router import router


def create_app() -> FastAPI:
    configure()
    app = FastAPI(title="Smart OS CEO Layer", version="0.2.0")
    app.include_router(router)

    @app.get("/", include_in_schema=False)
    def root():
        return RedirectResponse("/api/ceo/dashboard")

    return app
