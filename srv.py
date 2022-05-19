from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    valid_origins = ['https://example.com', 'https://exmaple.net']
    valid_headers = ['Content-Type']

    def is_valid_origin(self, origin):
        return origin in self.valid_origins

    def is_valid_header(self, header):
        return header.upper() in [h.upper() for h in self.valid_headers]

    def send_acao(self):
        origin = self.headers['Origin']
        acao = origin if self.is_valid_origin(origin) else ' '.join(self.valid_origins)
        self.send_header('Access-Control-Allow-Origin', acao)
        return

    def send_acah(self):
        acrh = self.headers['Access-Control-Request-Headers'].split(',')
        acah = ','.join([h for h in acrh if self.is_valid_header(h)])
        self.send_header('Access-Control-Allow-Headers', acah)

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
        self.send_acah()
        self.end_headers()
        return

httpd = HTTPServer(('localhost', 8003), CORSRequestHandler)
httpd.serve_forever()