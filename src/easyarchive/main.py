from real_filesystem import RealFileSystem
from sync import sync, read_paths_and_hashes

if __name__ == '__main__':
    source = ''
    dest = ''

    fs = RealFileSystem()
    sync(read_paths_and_hashes, fs, source, dest)

