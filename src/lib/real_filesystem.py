import os
import shutil
from pathlib import Path


class RealFileSystem:

    def home(self) -> str:
        return str(Path.home())

    def copy(self, src, dest):
        shutil.copy2(src, dest)

    def move(self, src, dest):
        shutil.move(src, dest)

    def delete(self, dest):
        os.remove(dest)

    def write_text(self, source, data):
        Path(source).write_text(data)

    def read_text(self, source):
        return Path(source).read_text(source)

    def write_binary(self, src, data: bytes) -> int:
        return Path(src).write_bytes(data)

    def read_binary(self, src) -> bytes:
        return Path(src).read_bytes()
