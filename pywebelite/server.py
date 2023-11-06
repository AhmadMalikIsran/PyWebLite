import http.server
import socketserver
import os

class Server:
    def run(self, router):
        PORT = 8000
        Handler = http.server.SimpleHTTPRequestHandler
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Serving at port", PORT)
            httpd.serve_forever()
