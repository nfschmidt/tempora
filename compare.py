#!/usr/bin/env python

import sys

CHUNK_SIZE = 1024

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
    byte_num = 0
    chunk1, chunk2 = 1, 1
    while chunk1 and chunk2:
        chunk1 = f1.read(CHUNK_SIZE)
        chunk2 = f2.read(CHUNK_SIZE)

        zipped = zip(chunk1, chunk2)
        for b1, b2 in zipped:
            if b1 != b2:
                print('Difference found in byte {}'.format(byte_num))
                print('File 1: {}'.format(ord(b1)))
                print('File 2: {}'.format(ord(b2)))

                exit(1)

            byte_num += 1
