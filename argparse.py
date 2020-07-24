# REF: https://docs.python.org/3/library/argparse.html
# argparse: An easy way to write user-friendly command-line interfaces,
#           which composing of arguments.

# Usage: type 'python3 argparse.py -h' in Terminal
#              python argparse.py 1 2 3 4
#              python argparse.py 1 2 3 4 --sum

import argparse

# creating a parser
parser = argparse.ArgumentParser(description='Process some integers.')

# adding arguments in an ArgumentParser
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')



# Converting argument strings to objects
args = parser.parse_args()


print(args.accumulate(args.integers))