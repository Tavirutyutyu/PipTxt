from urllib.request import urlopen
from pathlib import Path

class Reciever:
    def __init__(self, ip, port, reciever_path):
        self.ip = ip
        self.port = port
        self.reciever_path = Path(reciever_path)

    def get_file(self, filename):
        url = f"http://{self.ip}:{self.port}/file?name={filename}"
        with urlopen(url) as response:
            data = response.read().decode("utf-8")
            self.write_file(filename, data)


    def write_file(self, filename, content):
        filepath = self.reciever_path / filename
        with filepath.open("w", encoding="utf-8") as file:
            file.write(content)
