from threading import Thread
from http.server import HTTPServer

class ServerController:
    def __init__(self, handler, address=("0.0.0.0", 8080)):
        self.server = HTTPServer(address, handler)
        self.thread = None

    def start(self):
        if self.is_running():
            return
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def stop(self):
        if not self.is_running():
            return
        self.server.shutdown()
        self.thread.join()
        self.thread = None

    def exit(self):
        if self.is_running():
            self.stop()
        self.server.server_close()

    def is_running(self):
        return self.thread is not None