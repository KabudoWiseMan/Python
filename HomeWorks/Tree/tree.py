#!/usr/bin/env/python3
#
from os import listdir, sep, walk
from os.path import basename, isdir
import sys

def count(path):
    count_dirs = 0
    count_files = 0
    for root, dirs, files in walk(path):
            count_dirs += len(dirs)
            count_files += len(files)

    return count_dirs, count_files

def tree(dir, padding, print_files = False,
         is_last = False, is_first = False):
    if is_first:
        print(dir)
    elif is_last:
        print(padding[:-1] + '└── ' + basename(dir))
    else:
        print(padding[:-1] + '├── ' + basename(dir))

    if print_files:
        files = listdir(dir)
    else:
        files = [x for x in listdir(dir) if isdir(dir + sep + x)]
    files = sorted(files)
    
    if not is_first:
        padding += '   '
    count = 0
    last = len(files) - 1
    for i, file in enumerate(files):
        count += 1
        path = dir + sep + file
        is_last = i == last
        if isdir(path):
            if count == len(files):
                if is_first:
                    tree(path, padding, print_files, is_last, False)
                else:
                    tree(path, padding + ' ', print_files, is_last, False)
            else:
                tree(path, padding + '│', print_files, is_last, False)
        elif is_last:
            print(padding + '└── ' + file)
        else:
            print(padding + '├── ' + file)

if('-o' in sys.argv):
    sys.stdout = open(sys.argv[sys.argv.index('-o') + 1], 'w')
    
if len(sys.argv) == 1:
    tree('.', '', True, False, True)
    count_dirs, count_files = count('.')
    print('')
    print("{0} directories, {1} files".format(count_dirs, count_files))
elif len(sys.argv) == 2:
    if sys.argv[1] == '-d':
        tree('.', '', False, False, True)
        count_dirs, count_files = count('.')
        print('')
        print("{0} directories".format(count_dirs))
    elif isdir(sys.argv[1]):
        tree(sys.argv[1], '', True, False, True)
        count_dirs, count_files = count(sys.argv[1])
        print('')
        print("{0} directories, {1} files".format(count_dirs, count_files))       
elif len(sys.argv) == 3:
    if sys.argv[1] == '-d' and isdir(sys.argv[2]):
        tree(sys.argv[2], '', False, False, True)
        count_dirs, count_files = count(sys.argv[2])
        print('')
        print("{0} directories".format(count_dirs))
    elif sys.argv[2] == '-d' and isdir(sys.argv[1]):
        tree(sys.argv[1], '', False, False, True)
        count_dirs, count_files = count(sys.argv[1])
        print('')
        print("{0} directories".format(count_dirs))
    elif sys.argv[1] == '-o':
        tree('.', '', True, False, True)
        count_dirs, count_files = count('.')
        print('')
        print("{0} directories, {1} files".format(count_dirs, count_files))
    else:
        print('[error]')
elif len(sys.argv) == 4:
    if (sys.argv[1] == '-d' and sys.argv[2] == '-o' or
        sys.argv[1] == '-o' and sys.argv[2] == '-d'):
        tree('.', '', False, False, True)
        count_dirs, count_files = count('.')
        print('')
        print("{0} directories".format(count_dirs))
    elif sys.argv[1] == '-d' and sys.argv[3] == '-o':
        tree('.', '', False, False, True)
        count_dirs, count_files = count('.')
        print('')
        print("{0} directories".format(count_dirs))
    else:
        print('[error]')
elif len(sys.argv) == 5:
    if sys.argv[1] == '-d' and isdir(sys.argv[2]) and sys.argv[3] == '-o':
        tree(sys.argv[2], '', False, False, True)
        count_dirs, count_files = count(sys.argv[2])
        print('')
        print("{0} directories".format(count_dirs))
    elif sys.argv[1] == '-o' and sys.argv[3] == '-d' and isdir(sys.argv[4]):
        tree(sys.argv[4], '', False, False, True)
        count_dirs, count_files = count(sys.argv[4])
        print('')
        print("{0} directories".format(count_dirs))
    else:
        print('[error]')
else:
    print(sys.argv[len(sys.argv) - 1], "[error opening dir]")

sys.stdout.close()
