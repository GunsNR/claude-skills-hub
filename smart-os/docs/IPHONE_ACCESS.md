# iPhone access to Smart OS

## Same Wi-Fi (works today, zero install)

1. On the PC, find your LAN IP: `ipconfig` → IPv4 Address (e.g. `192.168.1.50`).
2. Allow the port through Windows Firewall (run once, as admin):
   ```powershell
   New-NetFirewallRule -DisplayName "Smart OS CEO" -Direction Inbound -Protocol TCP -LocalPort 8100 -Action Allow -Profile Private
   ```
3. Start the CEO layer (`python -m smartos_ceo.run` — it binds 0.0.0.0).
4. On the iPhone, open Safari → `http://192.168.1.50:8100`.
5. Share button → **Add to Home Screen**. The manifest makes it launch
   full-screen like a native app.

The dashboard is mobile-first: capture box, Top 3, quick wins, tax bar,
Dilshan queue. Refreshes itself every minute.

## Away from home (recommended: Tailscale)

Port-forwarding the router would expose the app to the internet with no
auth — don't. Tailscale gives you a private encrypted network instead:

1. Install Tailscale on the PC and iPhone, log in with the same account.
2. On the iPhone use `http://<tailscale-ip-of-pc>:8100` and Add to Home
   Screen again.
3. Optional: enable MagicDNS and use `http://<pc-name>:8100`.

Keep the PC awake (Settings → Power → never sleep when plugged in) or the
app goes down when the machine sleeps.

## Note on auth

The CEO layer has no login — protection comes from staying on
LAN/Tailscale. Before ever exposing it more broadly, add auth at the
Smart OS level (the integrated app is the right place for that).
