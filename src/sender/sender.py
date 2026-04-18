from pathlib import Path


class FileReader:

    def __init__(self, sender_path):
        self.sender_path: Path = Path(sender_path)

    def get_file_content(self, filename: str):
        filepath = self.sender_path / filename
        with filepath.open("r", encoding="utf-8") as file:
            return file.read()

    def file_exists(self, filename: str):
        filepath = self.sender_path / filename
        return filepath.exists()
