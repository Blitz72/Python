import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0, help='What is the second number?')
    parser.add_argument('--operation', type=str, default=1.0, help='What operatioin (add, sub, mul, or div)?')
    args = parser.parse_args()
    print(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

# print(f'Name of the script:          : {sys.argv[0]}')
# print(f'Arguments of the script      : {sys.argv[1:]}')

if __name__ == '__main__':
    main()