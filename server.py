from http.server import BaseHTTPRequestHandler, HTTPServer
from unicodedata import name
import openHTML
import time
import json

serverConfig = {
    "PORT" : 8000,
    "host" : "LOCALHOST"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        full_url = f"http://127.0.0.1:{self.server.server_port}{self.path}"
        print(full_url)
        
        self.wfile.write(openHTML.returnHTML("./get.html").encode())
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        full_url = f"http://127.0.0.1:{self.server.server_port}{self.path}"
        print(full_url)
        
        self.wfile.write(openHTML.returnHTML("./post.html").encode())

def main():
    PORT = serverConfig['PORT']
    server = HTTPServer(('localhost', PORT), Handler)
    print(f"Server running on port {PORT}")
    server.serve_forever()
    
if __name__ == '__main__':
    main()
    
