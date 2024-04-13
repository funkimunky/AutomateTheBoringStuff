import os


#https://pynative.com/python-count-number-of-lines-in-file/
def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


with open(r'/home/david/python/AutomateTheBoringStuff/files/harry.txt', 'rb') as fp:
    c_generator = _count_generator(fp.raw.read)
    # count each \n
    count = sum(buffer.count(b'\n') for buffer in c_generator)
    print('Total lines:', count + 1)