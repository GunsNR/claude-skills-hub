# iPhone instant capture (Siri / lock screen → Smart OS)

Brain-dump a task from anywhere without opening the app. One-time setup,
~3 minutes, uses the built-in **Shortcuts** app.

## Build the shortcut

1. Open **Shortcuts** on the iPhone → **+** (new shortcut).
2. Add action: **Ask for Input** → prompt: `Task?` → type Text.
3. Add action: **Get Contents of URL**:
   - URL: `http://YOUR-PC-IP:8100/api/ceo/capture`
     (your PC's LAN IP, or its Tailscale IP to work from anywhere)
   - Tap the arrow to expand → Method: **POST**
   - Request Body: **JSON** → add field: key `text`, value =
     **Provided Input** (the variable from step 2)
4. Add action: **Show Notification** → text: `Captured ✓`
5. Name it **"Smart OS"** → Done.

## Use it

- Say: **"Hey Siri, Smart OS"** → speak the task → done.
- Or add the shortcut to the home screen / lock-screen widget / Action
  Button for one-tap capture.

Whatever you say gets auto-classified like any capture: SEO production
work routes to Dilshan (and pings him), tax/finance items jump the queue,
quick replies land in quick wins.

## Notes

- The PC must be on and the app running (same requirement as the
  dashboard). Use the Tailscale IP if you capture away from home.
- Works for Dilshan too: he can build the same shortcut with
  `dilshan:` prefixed in his dictation, or just use his page at
  `http://YOUR-PC-IP:8100/api/ceo/dilshan`.
