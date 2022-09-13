import hashlib
import os
from pathlib import Path

BLOCKSIZE = 65536


def sync(reader, filesystem, source_root, dest_root):
    source_hashes = reader(source_root)
    dest_hashes = reader(dest_root)

    actions = determine_actions(source_hashes, dest_hashes, source_root, dest_root)

    for action, *paths in actions:
        if action == 'copy':
            filesystem.copy(*paths)
        if action == 'move':
            filesystem.move(*paths)
        if action == 'delete':
            filesystem.delete(paths[0])


def determine_actions(src_hashes, dst_hashes, src_folder, dst_folder):
    for sha, filename in src_hashes.items():
        if sha not in dst_hashes:
            sourcepath = str(Path(src_folder) / filename)
            destpath = str(Path(dst_folder) / filename)
            yield 'copy', sourcepath, destpath
        elif dst_hashes[sha] != filename:
            olddestpath = str(Path(dst_folder) / dst_hashes[sha])
            newdestpath = str(Path(dst_folder) / filename)
            yield 'move', olddestpath, newdestpath

    for sha, filename in dst_hashes.items():
        if sha not in src_hashes:
            yield 'delete', str(Path(dst_folder) / filename)


def hash_file(path):
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()


def read_paths_and_hashes(root):
    hashes = {}
    for folder, _, files in os.walk(root):
        for fn in files:
            hashes[hash_file(Path(folder) / fn)] = fn
    return hashes
