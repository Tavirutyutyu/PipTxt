import signal
from http.server import HTTPServer


class ServerCommand:

    def __init__(self, handler, address):
        self.server = HTTPServer(address, handler)
        self._register_signals()

    def start(self):
        print(f"Serving on {self.server.server_address[1]} (Ctrl+C to stop)")
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.shutdown()

    def shutdown(self, signum=None, frame=None):
        print("\nShutting down server...")
        self.server.shutdown()
        self.server.server_close()

    def _register_signals(self):
        signal.signal(signal.SIGTERM, self.shutdown)