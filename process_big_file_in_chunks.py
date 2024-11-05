#!/usr/bin/env python3

chunk_size = 500  # 500 bytes
pre_read_bytes = 100  # to read before chunk bytes (set zero if not required)

start = 0
i = 1

with open('bigfile.txt', 'rb') as f:
    while True:
        if start != 0:
            start = start - pre_read_bytes
            f.seek(start)  # move the file pointer to the start position

        file_chunk = f.read(chunk_size).decode('utf-8')
        if not file_chunk:
            break

        print(f'Chunk {i}:')
        print(file_chunk)

        start += chunk_size
        i += 1
