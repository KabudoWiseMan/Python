import sys
import argparse
from scan import count

parser = argparse.ArgumentParser(description="letters counter")
parser.add_argument('file_name', help="specify a file to open")
args = parser.parse_args()

try:
    file = open(args.file_name, 'r')
    count(file.read())
except FileNotFoundError:
    print("Couldn't open file ", args.file_name)
    sys.exit()
file.close()
