"""Outbound notifications (WhatsApp / email / webhook).

Channels — any combination, all configured purely via environment vars
(no credentials in code, config, or the database):

WhatsApp (CallMeBot, free — each recipient opts in once from their phone):
  SMARTOS_CALLMEBOT_PHONE / SMARTOS_CALLMEBOT_APIKEY   Dilshan
  SMARTOS_IZZY_PHONE / SMARTOS_IZZY_APIKEY             Izzy (morning brief)

Email (SMTP, e.g. Gmail with an app password — shared sender):
  SMARTOS_SMTP_HOST  e.g. smtp.gmail.com
  SMARTOS_SMTP_PORT  default 587 (STARTTLS)
  SMARTOS_SMTP_USER  the sending address
  SMARTOS_SMTP_PASS  app password
  SMARTOS_NOTIFY_EMAIL  Dilshan's address
  SMARTOS_IZZY_EMAIL    Izzy's address (morning brief)

Webhook (optional, for Zapier/Make fan-out):
  SMARTOS_NOTIFY_WEBHOOK  catch-hook URL; receives JSON

Unconfigured channels are skipped silently; failures are reported in the
return value but never raised.
"""

import os
import smtplib
import ssl
from email.message import EmailMessage

import httpx

CALLMEBOT_URL = "https://api.callmebot.com/whatsapp.php"


def whatsapp_to(phone: str | None, apikey: str | None, text: str) -> str:
    if not (phone and apikey):
        return "skipped (not configured)"
    try:
        resp = httpx.get(CALLMEBOT_URL,
                         params={"phone": phone, "text": text,
                                 "apikey": apikey},
                         timeout=15)
        return "sent" if resp.status_code == 200 else \
            f"failed (http {resp.status_code})"
    except Exception as exc:
        return f"failed ({type(exc).__name__})"


def email_to(to: str | None, subject: str, text: str) -> str:
    host = os.environ.get("SMARTOS_SMTP_HOST")
    user = os.environ.get("SMARTOS_SMTP_USER")
    password = os.environ.get("SMARTOS_SMTP_PASS")
    if not (host and user and password and to):
        return "skipped (not configured)"
    port = int(os.environ.get("SMARTOS_SMTP_PORT", "587"))
    try:
        msg = EmailMessage()
        msg["From"] = user
        msg["To"] = to
        msg["Subject"] = subject
        msg.set_content(text)
        with smtplib.SMTP(host, port, timeout=20) as smtp:
            smtp.starttls(context=ssl.create_default_context())
            smtp.login(user, password)
            smtp.send_message(msg)
        return "sent"
    except Exception as exc:
        return f"failed ({type(exc).__name__})"


def _webhook(payload: dict) -> str:
    url = os.environ.get("SMARTOS_NOTIFY_WEBHOOK")
    if not url:
        return "skipped (not configured)"
    try:
        resp = httpx.post(url, json=payload, timeout=15)
        return "sent" if resp.status_code < 300 else \
            f"failed (http {resp.status_code})"
    except Exception as exc:
        return f"failed ({type(exc).__name__})"


def notify_dilshan(title: str, details: str = "",
                   note_path: str | None = None) -> dict:
    """Fan a new-task notification out to all configured channels."""
    text = f"New task from Izzy: {title}"
    if details:
        text += f"\n\n{details}"
    if note_path:
        text += f"\n\nFull brief in Obsidian: {note_path}"
    return {
        "whatsapp": whatsapp_to(os.environ.get("SMARTOS_CALLMEBOT_PHONE"),
                                os.environ.get("SMARTOS_CALLMEBOT_APIKEY"),
                                text),
        "email": email_to(os.environ.get("SMARTOS_NOTIFY_EMAIL"),
                          f"[Smart OS] New task: {title}", text),
        "webhook": _webhook({"title": title, "details": details,
                             "note": note_path}),
    }


def notify_izzy(subject: str, text: str) -> dict:
    """Message Izzy himself (morning brief, blockers from Dilshan)."""
    return {
        "whatsapp": whatsapp_to(os.environ.get("SMARTOS_IZZY_PHONE"),
                                os.environ.get("SMARTOS_IZZY_APIKEY"),
                                text),
        "email": email_to(os.environ.get("SMARTOS_IZZY_EMAIL"),
                          subject, text),
    }
