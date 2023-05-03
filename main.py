from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO


hostname = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        data = self.rfile.read(content_len)
        self.send_response(201)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        response = BytesIO()
        self.wfile.write(response.getvalue())
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('“Hello, World wide web!”', 'utf-8'))
    

if __name__ == '__main__':
    web_server = HTTPServer((hostname, server_port), MyServer)
    print('Server started on http://%s:%s' % (hostname, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('Server stopped')
