from cli.sync import sync
from tests.fake_file_system import FakeFileSystem


def test_when_a_file_exists_in_the_source_but_not_the_destination():
    source = {"sha1": "my-file"}
    dest = {}
    filesystem = FakeFileSystem()

    reader = {"/source": source, "/dest": dest}
    sync(reader.pop, filesystem, "/source", "/dest")

    assert filesystem == [('COPY', "/source/my-file", "/dest/my-file")]


def test_when_a_file_has_been_renamed_in_the_source():
    source = {"sha1": "renamed-file"}
    dest = {"sha1": "original-file"}
    filesystem = FakeFileSystem()

    reader = {"/source": source, "/dest": dest}
    sync(reader.pop, filesystem, "/source", "/dest")

    assert filesystem == [
        ('MOVE', "/dest/original-file", "/dest/renamed-file")]


def test_when_a_file_exists_in_the_destination_but_not_the_source():
    source = {}
    dest = {"sha1": "original-file"}
    filesystem = FakeFileSystem()

    reader = {"/source": source, "/dest": dest}
    sync(reader.pop, filesystem, "/source", "/dest")

    assert filesystem == [
        ('DELETE', "/dest/original-file")]
