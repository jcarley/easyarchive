import os
import socket

import buffer
from file_info import FileInfo

HOST = ''
PORT = 5001

try:
    os.mkdir('uploads')
except FileExistsError:
    pass

s = socket.socket()
s.bind((HOST, PORT))
s.listen(10)

print("Waiting for a connection...")

while True:
    conn, addr = s.accept()
    print("Got a connection from ", addr)
    connbuf = buffer.Buffer(conn)

    while True:

        file_info_json = connbuf.get_utf8()
        if not file_info_json:
            break

        file_info = FileInfo.from_json(file_info_json)

        filename = os.path.join('uploads', file_info.filename)
        print('filename: ', filename)

        file_size = file_info.filesize
        print('file size: ', file_size)

        checksum = file_info.checksum
        print('file checksum: ', checksum)

        with open(filename, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = connbuf.get_bytes(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('File incomplete. Missing', remaining, 'bytes\n')
            else:
                print('File received successfully.\n')

    print('Connection closed')
    conn.close()
