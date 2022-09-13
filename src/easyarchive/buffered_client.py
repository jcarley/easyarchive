import os.path
import pathlib
import socket

import buffer
import hasher
from file_info import FileInfo

HOST = 'localhost'
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

with s:
    sbuf = buffer.Buffer(s)

    files_to_send = [f for f in pathlib.Path('client').iterdir()]

    for filename in files_to_send:
        checksum = hasher.hash_file(filename)
        file_size = os.path.getsize(filename)

        file_info = FileInfo(
            filename=os.path.basename(filename),
            filesize=file_size,
            checksum=checksum
        )

        file_info_json = file_info.to_json()

        sbuf.put_utf8(file_info_json)

        with open(filename, 'rb') as f:
            sbuf.put_bytes(f.read())
        print('File Sent')
