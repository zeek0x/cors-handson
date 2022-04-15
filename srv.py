from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    valid_origin_list = ['https://example.com', 'https://exmaple.net']

    def is_valid_origin(self, origin):
        return origin in self.valid_origin_list

    def do_GET(self):
        self.send_response(200)
        origin = self.headers['Origin']
        print(origin)
        acao = origin if self.is_valid_origin(origin) else ' '.join(self.valid_origin_list)
        self.send_header('Access-Control-Allow-Origin', 'https://example.com',)
        self.end_headers()
        self.wfile.write(b'Hello CORS!')
        return

httpd = HTTPServer(('localhost', 8003), CORSRequestHandler)
httpd.serve_forever()