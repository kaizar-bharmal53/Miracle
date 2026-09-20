import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Handle clean URLs like /about -> /about.html or /about/index.html
        path = self.path.split('?')[0].split('#')[0]
        full_path = os.path.join(DIRECTORY, path.lstrip('/'))

        if not os.path.exists(full_path) and os.path.exists(full_path + '.html'):
            self.path = path + '.html'

        return super().do_GET()

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

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
