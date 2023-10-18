import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--char", help="Print out 100 unicode characters starting at a base character num(decimal)! ex: -c 2600")
args = parser.parse_args()

char_num = int(args.char) if args.char else 0
mystring = '  '.join(f"{chr(char_num + i)} {char_num + i}" for i in range(100))
print(mystring)
print(chr(0x2660), chr(0x2663), chr(0x2665), chr(0x2666))
