#!/usr/bin/python

from pathlib import Path
from http.server import HTTPServer
from functools import partial
from network import GetHandler
from transfer import Reciever
from cli import Menu
from network import ServerCommand
import sys
import signal

REQUEST_KEYWORDS = ["request", "r", "-request", "--request", "-r", "--r", "R", "-R", "--R"]
SERVE_KEYWORDS = ["serve", "s", "-serve", "--serve", "-s", "--s", "S", "-S", "--S"]
BASE_DIR = Path(__file__).resolve().parent
RESOURCES_DIR = BASE_DIR.parent / "resources"

def run():
    args = sys.argv[1:]
    if args:
        run_as_command(args)
    else:
        run_as_menu()

def print_help():
    print("""
PipTxt — Python Text Transfer Utility

USAGE
    python main.py                Start interactive menu
    python main.py serve          Run file server
    python main.py request FILE   Request file from server

REQUEST FLAGS
    r, R, -r, --r
    request, -request, --request

SERVE FLAGS
    s, S, -s, --s
    serve, -serve, --serve

EXAMPLES
    python main.py
    python main.py serve
    python main.py request example.txt
""")

def request(filename):
    reciever = Reciever("192.168.1.127", "8080", RESOURCES_DIR / "reciever")
    reciever.get_file(filename)


def run_as_command(args):
    first_arg = args[0]
    if first_arg in REQUEST_KEYWORDS:
        print("Request Mode")
        filename = args[1]
        request(filename)
    elif first_arg in SERVE_KEYWORDS:
        handler = partial(GetHandler, RESOURCES_DIR / "sender")
        address = ("0.0.0.0", 8080)
        serve_command = ServerCommand(handler, address)
        serve_command.start()
    else:
        print_help()
    

def run_as_menu():
    reciever = Reciever("192.168.1.127", "8080", RESOURCES_DIR / "reciever")
    handler = partial(GetHandler, RESOURCES_DIR / "sender")
    address = ("0.0.0.0", 8080)
    menu = Menu(reciever, handler, address)
    menu.run()

if __name__ == "__main__":
    run()