"""Run the CEO layer standalone: python -m smartos_ceo.run

Binds to 0.0.0.0 so the dashboard is reachable from an iPhone on the same
LAN (see docs/IPHONE_ACCESS.md).
"""

import os

import uvicorn

from .app import create_app
from .scheduler import start as start_scheduler

app = create_app()

if __name__ == "__main__":
    if os.environ.get("SMARTOS_SCHEDULER", "on") != "off":
        start_scheduler()
    port = int(os.environ.get("SMARTOS_CEO_PORT", "8100"))
    uvicorn.run(app, host="0.0.0.0", port=port)
