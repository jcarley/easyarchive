from easyarchive.file_info import FileInfo, Files, FilesEncoder, FilesIO
from tests.fake_file_system import FakeFileSystem


def test_serializing_file_info_database_to_json():
    file1 = FileInfo(
        checksum="12345678sdfghjk",
        filename="file1.jpg",
        filesize=12345678,
    )

    file2 = FileInfo(
        checksum="87654321hgfdstre",
        filename="file2.jpg",
        filesize=9876542,
    )

    files = Files()
    files.add(file1)
    files.add(file2)

    print("")
    files_json = FilesEncoder.to_json(files)
    print(files_json)

    files_from_json = FilesEncoder.from_json(files_json)
    print(files_from_json)


def test_saves_files_to_filesystem():
    file1 = FileInfo(
        checksum="12345678sdfghjk",
        filename="file1.jpg",
        filesize=12345678,
    )

    file2 = FileInfo(
        checksum="87654321hgfdstre",
        filename="file2.jpg",
        filesize=9876542,
    )

    files = Files()
    files.add(file1)
    files.add(file2)

    fake_filesystem = FakeFileSystem()
    files_io = FilesIO(fake_filesystem)
    files_io.save('files.json', files)

    assert fake_filesystem == [('WRITE', 'files.json', FilesEncoder.to_json(files))]


def test_loads_files_from_filesystem():
    files_json = """
{
    "12345678sdfghjk": {
        "checksum": "12345678sdfghjk",
        "createdAt": {
            "data": "2022-09-13T15:34:37.640879",
            "type": "datetime"
        },
        "filename": "file1.jpg",
        "filesize": 12345678
    },
    "87654321hgfdstre": {
        "checksum": "87654321hgfdstre",
        "createdAt": {
            "data": "2022-09-13T15:34:37.640895",
            "type": "datetime"
        },
        "filename": "file2.jpg",
        "filesize": 9876542
    }
}
"""

    fake_filesystem = FakeFileSystem(read_result=files_json)
    files_io = FilesIO(fake_filesystem)
    files = files_io.load('files.json')

    assert fake_filesystem == [('READ', 'files.json')]

    assert files.get("87654321hgfdstre") is not None
    assert files.get("12345678sdfghjk") is not None
