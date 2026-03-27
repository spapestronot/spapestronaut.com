#!/usr/bin/env python3
"""
Simple local dev server for previewing the site.

Usage:
  python3 serve.py

Then open http://localhost:8000 in your browser.
Press Ctrl+C to stop.
"""

import http.server
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIRECTORY)

handler = http.server.SimpleHTTPRequestHandler
server = http.server.HTTPServer(("", PORT), handler)

print(f"Serving site at http://localhost:{PORT}")
print(f"Press Ctrl+C to stop.\n")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStopped.")
    server.server_close()
