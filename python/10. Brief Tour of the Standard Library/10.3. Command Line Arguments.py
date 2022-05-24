import sys
import argparse

# run with python i.e. "python 10.3. Command Line Arguments.py one two three"
# output results from running python demo.py one two three at the command line:
print(sys.argv)  # ['demo.py', 'one', 'two', 'three']

# python top.py --lines=5 alpha.txt beta.txt
parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
