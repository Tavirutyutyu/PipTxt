from network import GetHandler, ServerCommand, ServerController

import os


class Menu:
    def __init__(self, reciever: Reciever, handler: GetHandler, address: tuple[str, int] = ("0.0.0.0", 8080)):
        self.reciever: Reciever = reciever
        self.server_controller: ServerController = ServerController(handler, address)
        self.serving_thread: Thread | None = None

    def start_server(self):
        self.server_controller.start()

    def stop_server(self):
        self.server_controller.stop()

    def toggle_server(self):
        if self.server_controller.is_running():
            self.stop_server()
            print("\nServer stopped")
        else:
            self.start_server()
            print("\nServer started")

        input("\nPress Enter to continue...")

    def request_file(self):
        filename = input("\nFilename: ").strip()
        try:
            self.reciever.get_file(filename)
            print("✔ File received")
        except Exception:
            print("✘ Transfer failed")

        input("\nPress Enter to continue...")
        

    def run(self):
        while True:
            self.print_menu()
            choice = input("> ").strip()
            match choice:
                case "1": self.request_file()
                case "2": self.toggle_server()
                case "3": 
                    self.server_controller.exit()
                    return

    def print_menu(self):
        os.system("clear")

        status = "RUNNING" if self.server_controller.is_running() else "STOPPED"
        action = "Stop server" if self.server_controller.is_running() else "Start server"

        print("╔══════════════════════════════════════╗")
        print("║            PipTxt Control            ║")
        print("╠══════════════════════════════════════╣")
        print(f"║ Server status : {status:<18}   ║")
        print("╠══════════════════════════════════════╣")
        print("║ 1. Request file                      ║")
        print(f"║ 2. {action:<31}   ║")
        print("║ 3. Exit                              ║")
        print("╚══════════════════════════════════════╝")
