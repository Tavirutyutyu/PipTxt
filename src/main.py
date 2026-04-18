from http.server import HTTPServer
from handler import GetHandler
from functools import partial

def run():
    handler = partial(GetHandler, "/home/tavirutyutyu/Programming/pip_txt/resources/sender")
    server = HTTPServer(("0.0.0.0", 8080), handler)
    server.serve_forever()

if __name__ == "__main__":
    run()