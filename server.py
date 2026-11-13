"""
Local HTTP Server for L&T 500 Roles & Responsibilities Interactive Dashboard
Serves on http://localhost:8080
"""
import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Concise logging
        sys.stderr.write(f"[L&T 500-Roles Server] {format % args}\n")

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 80)
        print(f" L&T 500 ROLES DASHBOARD SERVER RUNNING")
        print(f" Access URL: http://localhost:{PORT}")
        print(f" Serving Directory: {DIRECTORY}")
        print("=" * 80)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
