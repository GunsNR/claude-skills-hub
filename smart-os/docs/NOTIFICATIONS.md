# Notifying Dilshan automatically (WhatsApp + email)

When a task is delegated to Dilshan — by auto-classification, the
`/delegate` endpoint, or tapping **→ DS** on the dashboard — Smart OS
fans a notification out to every channel you've configured. Unconfigured
channels are skipped silently; a failed send never blocks the task.

All configuration is environment variables. No credentials in files, ever.

## WhatsApp (free, ~3 minutes, via CallMeBot)

CallMeBot is a free personal-notification gateway — no Meta business
account needed. **Dilshan** does the one-time opt-in on his phone:

1. Dilshan adds the CallMeBot number to his contacts: **+34 644 96 09 73**
   (current number is listed at https://www.callmebot.com/blog/free-api-whatsapp-messages/ — check there if it changed).
2. He sends it this WhatsApp message: `I allow callmebot to send me messages`
3. The bot replies with his personal **apikey**.
4. On your PC (new PowerShell after each, or set both then reopen once):

```powershell
[Environment]::SetEnvironmentVariable("SMARTOS_CALLMEBOT_PHONE", "+94XXXXXXXXX", "User")
[Environment]::SetEnvironmentVariable("SMARTOS_CALLMEBOT_APIKEY", "123456", "User")
```

`SMARTOS_CALLMEBOT_PHONE` is **Dilshan's** WhatsApp number with country
code; the apikey is the one the bot sent **him**.

## Email (via Gmail app password)

1. On your Google account: https://myaccount.google.com/apppasswords →
   create an app password (requires 2-step verification to be on).
2. Set:

```powershell
[Environment]::SetEnvironmentVariable("SMARTOS_SMTP_HOST", "smtp.gmail.com", "User")
[Environment]::SetEnvironmentVariable("SMARTOS_SMTP_USER", "you@gmail.com", "User")
[Environment]::SetEnvironmentVariable("SMARTOS_SMTP_PASS", "xxxx xxxx xxxx xxxx", "User")
[Environment]::SetEnvironmentVariable("SMARTOS_NOTIFY_EMAIL", "dilshan@example.com", "User")
```

The app password is NOT your Gmail password — it's the 16-character one
Google generates. Treat it like the OpenRouter key: env var only.

## Optional: Zapier/Make webhook (for anything else)

If you'd rather route through Zapier (e.g. Slack, SMS, a different
WhatsApp provider like Twilio):

1. Zapier → new Zap → trigger **Webhooks by Zapier → Catch Hook** → copy the URL.
2. `[Environment]::SetEnvironmentVariable("SMARTOS_NOTIFY_WEBHOOK", "<that URL>", "User")`
3. Add actions in Zapier using the incoming fields `title`, `details`, `note`.

## Verify it works

Restart the CEO layer, then either tap **→ DS** on any dashboard task, or:

```powershell
curl.exe -X POST http://localhost:8100/api/ceo/delegate -H "Content-Type: application/json" -d "{\"title\": \"Notification test - ignore\"}"
```

The response includes per-channel status, e.g.
`"notified": {"whatsapp": "sent", "email": "sent", "webhook": "skipped (not configured)"}`.
The dashboard toast shows the same when you reassign a task.

## Reassigning tasks

Every task card now has a reassign button: **→ DS** hands it to Dilshan
(and notifies him), **→ Me** on his queue takes it back (no notification).
API: `POST /api/ceo/tasks/{id}/owner` with `{"owner": "dilshan"}` or
`{"owner": "izzy"}`.
