#!/usr/bin/env python3
"""Create or update a WordPress post from a dist/ HTML file via the REST API.

Reads IWS_WP_URL, IWS_WP_USER, IWS_WP_APP_PASSWORD from the environment and
never prints them. Prints only: post id, status, link; on errors the HTTP
status and the WordPress error code.

Usage:
  python publish_wp.py --slug my-post --title "Title" --file dist/my-post.html \
      --excerpt "Meta description" --status draft [--update]
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


def env():
    vals = {k: os.environ.get(k, "") for k in ("IWS_WP_URL", "IWS_WP_USER", "IWS_WP_APP_PASSWORD")}
    missing = [k for k, v in vals.items() if not v]
    if missing:
        print("missing environment variables: " + ", ".join(missing))
        sys.exit(2)
    return vals


def call(method, url, auth, payload=None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Basic " + auth)
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json; charset=utf-8")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        code = ""
        try:
            code = json.loads(e.read().decode("utf-8")).get("code", "")
        except Exception:
            pass
        print("error: HTTP %s %s" % (e.code, code))
        sys.exit(1)
    except urllib.error.URLError as e:
        print("error: site unreachable (%s)" % type(e.reason).__name__)
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--file", required=True)
    ap.add_argument("--excerpt", default="")
    ap.add_argument("--status", choices=["publish", "draft"], required=True)
    ap.add_argument("--update", action="store_true")
    a = ap.parse_args()

    v = env()
    base = v["IWS_WP_URL"].rstrip("/") + "/wp-json/wp/v2/posts"
    auth = base64.b64encode(("%s:%s" % (v["IWS_WP_USER"], v["IWS_WP_APP_PASSWORD"])).encode("utf-8")).decode("ascii")
    with open(a.file, encoding="utf-8") as f:
        content = f.read()

    q = urllib.parse.urlencode({"slug": a.slug, "status": "any", "context": "edit"})
    _, existing = call("GET", base + "?" + q, auth)
    payload = {"title": a.title, "slug": a.slug, "status": a.status, "content": content, "excerpt": a.excerpt}

    if a.update:
        if not existing:
            print("error: no existing post with slug %s to update" % a.slug)
            sys.exit(1)
        _, post = call("POST", "%s/%d" % (base, existing[0]["id"]), auth, payload)
    else:
        if existing:
            p = existing[0]
            print("exists: id=%s status=%s link=%s (use --update)" % (p["id"], p["status"], p.get("link", "")))
            sys.exit(3)
        _, post = call("POST", base, auth, payload)

    print("id=%s status=%s link=%s" % (post["id"], post["status"], post.get("link", "")))


if __name__ == "__main__":
    main()
