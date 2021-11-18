###############################################################

# Python Tutorial: Context Managers - Efficiently Managing Resources

# https://www.youtube.com/watch?v=-aKFBoZpiqA

###############################################################


# class Open_File():

 #     def __init__(self, filename, mode, encoding_type='UTF-8'):
#         self.filename = filename
#         self.mode = mode
#         self.encoding_type = encoding_type


#     def __enter__(self):
#         self.file = open(self.filename, self.mode, encoding=self.encoding_type)
#         return self.file


#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()


# with Open_File('sample.txt', 'w', 'UTF-8') as f:
#     f.write("Aliqua aliqua velit do incididunt ex fugiat commodo commodo cupidatat excepteur exercitation.\n")
#     f.write("What's the deal with all this 'Lorem ipsum' stuff?\n")

# print(f.closed)
# print(f)

# with Open_File('sample.txt', 'a', 'UTF-8') as f:
#     f.write("Dude, you can even add stuff to a file without overwiting it!\n")


# f = open('sample.txt', 'w', encoding='UTF-8')
# f.write("What's the deal with all this 'Lorem ipsum' stuff?")
# f.close()

# with open('sample.txt', 'w') as f:
#     f.write("What's the deal with all this 'Lorem ipsum' stuff?")

# print(f.closed)
# print(f)

# And now Context Manager as a Function

# from contextlib import contextmanager


# @contextmanager
# def open_file(filename, mode, encoding_type='UTF-8'):   # use UTF-8 encoding as default if none speicified
#     try:
#         f = open(filename, mode, encoding=encoding_type)
#         yield f
#     finally:
#         f.close()


# with open_file('sample.txt', 'w') as f:
#     f.write('''In this Python Programming Tutorial, we will be learning how to use context managers to properly manage resources.\n''')
    
# print(f.closed)
# print(f)


# A practical example with files

import os
from contextlib import contextmanager

# os.mkdir('Sample-Dir-One')
# os.mkdir('Sample-Dir-Two')

# cwd = os.getcwd()
# os.chdir('Sample-Dir-One')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)

# can use a context manager to do the above work for us

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('Sample-Dir-One'):
    print(os.getcwd())
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.getcwd())
    print(os.listdir())