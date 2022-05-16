from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    valid_origin_list = ['https://example.com', 'https://exmaple.net']

    def is_valid_origin(self, origin):
        return origin in self.valid_origin_list

    def send_acao(self):
        origin = self.headers['Origin']
        acao = origin if self.is_valid_origin(origin) else ' '.join(self.valid_origin_list)
        self.send_header('Access-Control-Allow-Origin', acao)
        return

    def do_GET(self):
        self.send_response(200)
        self.send_acao()
        self.end_headers()
        self.wfile.write(b'Hello CORS!')
        return

    def do_POST(self):
        self.send_response(201)
        self.send_acao()
        self.end_headers()
        self.wfile.write(b'Nice POST!')
        return

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_acao()
        self.end_headers()
        return

httpd = HTTPServer(('localhost', 8003), CORSRequestHandler)
httpd.serve_forever()