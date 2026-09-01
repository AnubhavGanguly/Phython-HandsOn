import os
from pathlib import Path

class FileHelper:

    def __init__(self, file_path, content =""):
        self.file_path = file_path
        self.content = content

    def create_file(self):
        "Create a new file and optionally write content to it."
        path = Path(self.file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(self.content)
        print(f"File created: {path}")


    def readFile(self):
        "Read and return the file content."
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()
            

    def updateFile(self,content):
        "Add content to the end of an existing file."
        with open(self.file_path, "a", encoding="utf-8")as file:
            file.write("\n" + content)

    def writeFile(self,content):
        "Overwrite the existing file with new content."
        with open(self.file_path, "w", encoding="utf-8")as file:
            file.write(content)

    def deleteFile(self):
        "Delete a file."
        path = Path(self.file_path)

        if path.exists():
            path.unlink()
            print(f"File deleted: {path}")
        else:
            print(f"File does not exist: {path}")

    