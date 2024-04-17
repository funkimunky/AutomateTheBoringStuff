# to use python split_large_text.py <relative file path> <number of splits>
import os
import sys
import tempfile
from itertools import zip_longest
import math

#https://pynative.com/python-count-number-of-lines-in-file/

def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


def read_file(filename):
    with open(filename, 'rb') as fp:
        c_generator = _count_generator(fp.raw.read)
        # count each \n
        count = sum(buffer.count(b'\n') for buffer in c_generator)
        print('Total lines:', count + 1)

    return count


def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def split_large_file(filename, num_lines):
    with open(filename) as f:
        for i, g in enumerate(grouper(num_lines, f, fillvalue=''), 1):
            filename_split = os.path.splitext(filename)
            with open((filename_split[0]+'_{0}'+filename_split[1]).format(i), 'w') as fout:
                fout.writelines(g)


def split_file():
    parameters = sys.argv
    if len(parameters) == 3:
        count = read_file(parameters[1])
        split_num_lines = math.ceil(count/int(parameters[2]))
        split_large_file(parameters[1], split_num_lines)

    else:
        print('python3 splitText.py filename_with_path number_of_parts')
        exit(1)


split_file()

