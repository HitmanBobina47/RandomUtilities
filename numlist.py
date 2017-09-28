import argparse

parser = argparse.ArgumentParser(description="Generates a list of numbers with given format and base")
parser.add_argument("format", type=str, help="Format of string. \
For 255, {dec}, {hex}, {oct}, {bin}, {dec0}, {hex0}, {oct0}, and {bin0}\
 are replaced with 255, FF, 377, 11111111, 0d255, 0xFF, 0o377, and 0b11111111")
parser.add_argument("-s", "--start", type=int, default=0, help="Starting value")
parser.add_argument("-e", "--end", type=int, default=255, help="Ending value")
parser.add_argument("-f", "--file", type=str, help="File to write to. (can be used with -o)")
parser.add_argument("--onelinefile", action="store_true", help="By default, a newline is appended to the format \
when outputting to a file to match print() used by -o. If you don't want that, use this option. Does not effect -o option.")
parser.add_argument("-o", "--stdout", action="store_true", help="Output list to stdout. (can be used with -f)")

args = parser.parse_args()

if args.file:
    f = open(args.file, "w")

fileEOL = "\n"
if args.onelinefile:
    fileEOL = ""

for i in range(args.end + args.start):
    outstr = args.format.format(dec=i, hex=hex(i)[2:], oct=oct(i)[2:], bin=bin(i)[2:], dec0="0d" + str(i), hex0=hex(i), oct0=oct(i), bin0=bin(i))
    if args.file:
        f.write(outstr+fileEOL)
    if args.stdout:
        print(outstr)

if args.file:
    f.close()