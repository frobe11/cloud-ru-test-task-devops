import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        author = os.getenv("AUTHOR", "frb11")
        print(author)

        html = f"""
        <html>
            <head><title>01-application-cloud-ru-{author}</title></head>
            <body>
                <h1>Информация о сервере</h1>
                <p>Имя хоста: {hostname}</p>
                <p>ip адрес хоста: {ip_address}</p>
                <p>Имя автора: {author}</p>
            </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-16"))

server_address = ("", 8000)
load_dotenv()
httpd = HTTPServer(server_address, MyHandler)
print("Server running on port 8000...")
httpd.serve_forever()
