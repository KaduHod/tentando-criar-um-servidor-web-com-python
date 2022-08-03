from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

serverConfig = {
    "PORT" : 8000,
    "host" : "LOCALHOST"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','aplication/json')
        self.end_headers()
        self.wfile.write(json.dumps(serverConfig).encode())

def main():
    PORT = serverConfig['PORT']
    server = HTTPServer(('', PORT), Handler)
    print(f"Server running on port {PORT}")
    server.serve_forever()
    
# if __name__ == '__main__':
    # main()
    
print(__name__)