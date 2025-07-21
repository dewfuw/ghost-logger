from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        data = self.rfile.read(length).decode()
        print("[+] Received data:\n", data)
        self.send_response(200)
        self.end_headers()

print("[*] Listening on http://192.168.1.7:8000")
HTTPServer(('192.168.1.7', 8000), Handler).serve_forever()
