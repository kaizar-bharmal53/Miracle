import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def clean_url_path(self):
        # Support /public/ rewrite to /certificates/
        if self.path.startswith('/public/'):
            self.path = self.path.replace('/public/', '/certificates/', 1)

        raw_path = self.path.split('?')[0].split('#')[0]

        # Route static assets regardless of sub-path (e.g. /mandatory-disclosures/css/style.css -> /css/style.css)
        for asset_dir in ['css', 'js', 'images', 'fonts', 'certificates', 'documents']:
            prefix = f'/{asset_dir}/'
            if prefix in raw_path and not raw_path.startswith(prefix):
                self.path = raw_path[raw_path.find(prefix):]
                return

        # Handle clean URLs like /about or /mandatory-disclosures (with or without trailing slash)
        stripped = raw_path.strip('/')
        if stripped:
            full_path = os.path.join(DIRECTORY, stripped)
            if os.path.exists(full_path + '.html'):
                self.path = '/' + stripped + '.html'
            elif os.path.exists(os.path.join(full_path, 'index.html')):
                self.path = '/' + stripped + '/index.html'

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        self.clean_url_path()
        return super().do_GET()

    def do_HEAD(self):
        self.clean_url_path()
        return super().do_HEAD()

class ReusableTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

def find_available_server(start_port=DEFAULT_PORT):
    for port in [start_port, 8080, 8001, 8002, 3000, 5000]:
        try:
            httpd = ReusableTCPServer(("", port), CleanURLHandler)
            return httpd, port
        except OSError as e:
            if e.errno == 48: # Address already in use
                continue
            raise
    # If standard ports are busy, let OS choose
    httpd = ReusableTCPServer(("", 0), CleanURLHandler)
    return httpd, httpd.server_address[1]

if __name__ == '__main__':
    httpd, port = find_available_server()
    print(f"\n==================================================")
    print(f"  Miracle Global School website is live!")
    print(f"  URL: http://localhost:{port}")
    print(f"==================================================")
    print("Press Ctrl+C to stop.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
