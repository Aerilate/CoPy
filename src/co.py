#!/usr/bin/env python

import sys
import os
from os import path
from stack import push


def main():
    if len(sys.argv) != 2:
        print('Usage: co.py <path>')

    copy_path = sys.argv[1]
    if path.isdir(copy_path):
        print('Specified path is a directory. Copying path name...')
    elif path.isfile(copy_path):
        print('Specified path is a file. Copying path name...')
    else:
        print('Specified path is not a valid directory or a file. Exiting...')
        quit()

    push(copy_path)
    print '\t...copied path', os.path.abspath(copy_path)
    

if __name__ == '__main__':
    main()
