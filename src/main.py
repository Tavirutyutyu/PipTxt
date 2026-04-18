#!/usr/bin/python

from pathlib import Path
from http.server import HTTPServer
from functools import partial
from handler import GetHandler
from reciever import Reciever
import sys

REQUEST_KEYWORDS = ["request", "r", "-request", "--request", "-r", "--r", "R", "-R", "--R"]
SERVE_KEYWORDS = ["serve", "s", "-serve", "--serve", "-s", "--s", "S", "-S", "--S"]
BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR.parent / "resources"

def run():
    args = sys.argv[1:]
    if args:
        first_arg = args[0]
        if first_arg in REQUEST_KEYWORDS:
            print("Request Mode")
            filename = args[1]
            request(filename)
        elif first_arg in SERVE_KEYWORDS:
            print("Serve Mode")
            serve()
        else:
            print_help()
    else:
        print_help()

def print_help():
    usage_str = f"""
    Welcome to the PipTxt or Python Text Transfer application.

    Usage:

    There are 2 modes: request and serve
        
        Request mode: main.py [request_mode_flag] [filename]
            (request mode flags: {", ".join(REQUEST_KEYWORDS)})

        
        Servev mode: main.py [serve_mode_flag]
            (serve mode flags: {", ".join(SERVE_KEYWORDS)})
    """
    print(usage_str)

def request(filename):
    reciever = Reciever("192.168.1.127", "8080", RESOURCES_DIR / "reciever")
    reciever.get_file(filename)


def serve():
    handler = partial(GetHandler, RESOURCES_DIR / "sender")
    server = HTTPServer(("0.0.0.0", 8080), handler)
    server.serve_forever()

if __name__ == "__main__":
    run()