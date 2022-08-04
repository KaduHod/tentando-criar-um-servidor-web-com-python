from http.server import BaseHTTPRequestHandler, HTTPServer
from unicodedata import name
from controllers import exercicios
from util import path, controllers
import openHTML
import time
import json


serverConfig = {
    "PORT" : 8000,
    "host" : "LOCALHOST"
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handleRequest('GET')
       
    def do_POST(self):
        self.handleRequest('POST')

    def handleRequest(self, METHOD):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        pathSplit = path.handlePath(self.path)
        
        file = controllers.handle(
            pathSplit["controller"],
            pathSplit["method"],
            pathSplit["argument"]
        )
        
        self.wfile.write(file.encode())



def main():
    PORT = serverConfig['PORT']
    server = HTTPServer(('localhost', PORT), Handler)
    print(f"Server running on localhost:{PORT}")
    server.serve_forever()
    
if __name__ == '__main__':
    main()
    
