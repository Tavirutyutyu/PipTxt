from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from pathlib import Path
from storage import FileReader

class GetHandler(BaseHTTPRequestHandler):
    def __init__(self, sender_path, *args, **kwargs):
        self.file_reader = FileReader(sender_path)
        super().__init__(*args, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/file":
            params = parse_qs(parsed.query)
            name = params.get("name", [None])[0]
            if not name:
                self.set_status_and_header(400)
                return
            if not self.file_reader.file_exists(name):
                self.set_status_and_header(404)
                return
            try:
                content = self.file_reader.get_file_content(name)
                self.set_status_and_header(200, [{"Content-Type": "text/plain"}])
                self.wfile.write(content.encode("utf-8"))
            except Exception as e:
                print("Exception!!!", e)
                self.set_status_and_header(400)
        else:
            self.set_status_and_header(500)

    def set_status_and_header(self, status, header_dict_list: list[dict[str, str]] = []):
        self.send_response(status)
        for header in header_dict_list:
            for k, v in header.items():
                self.send_header(k, v)
        self.end_headers()
