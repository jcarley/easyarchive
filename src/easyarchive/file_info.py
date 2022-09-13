from dataclasses import field, dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, Undefined, LetterCase

from easyarchive import jsonx


@dataclass_json(undefined=Undefined.EXCLUDE, letter_case=LetterCase.CAMEL)
@dataclass
class FileInfo:
    # we use checksum as the primary key
    checksum: str
    filename: str
    filesize: int
    created_at: datetime = field(default_factory=datetime.utcnow)


class Files(dict):
    def add(self, fi: FileInfo):
        self[fi.checksum] = fi

    def remove(self, checksum: str):
        if checksum in self:
            del self[checksum]

    def update_fi(self, fi: FileInfo):
        if fi.checksum in self:
            self[fi.checksum] = fi


class FilesEncoder:
    @staticmethod
    def to_json(files: Files):
        converted_items = {key: value.to_dict() for key, value in files.items()}
        return jsonx.dumps(converted_items, indent=4, sort_keys=True)

    @staticmethod
    def from_json(json_data) -> Files:
        data = jsonx.loads(json_data)
        files = Files(data)

        for key, value in files.items():
            files[key] = FileInfo.from_dict(value)

        return files


class FilesIO:

    def __init__(self, filesystem):
        self.filesystem = filesystem

    def save(self, source: str, files: Files):
        json_data = FilesEncoder.to_json(files)
        self.filesystem.write_text(source, json_data)

    def load(self, source: str) -> Files:
        json_data = self.filesystem.read_text(source)
        return FilesEncoder.from_json(json_data)
