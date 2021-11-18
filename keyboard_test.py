import sys

x = 0
while x != 'p':
    x = sys.stdin.read(1)[0]
    print('You pressed:', x)
    if x == 'p':
        print('program terminated.')