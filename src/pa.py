#!/usr/bin/env python

import sys
import subprocess
import os
from os import path
from stack import s_len
from stack import is_empty
from stack import pop
from stack import top


def exec_cmd(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

def main():
    if len(sys.argv) != 1:
        print('Usage: pa.py')

    paste_path = ''
    if (is_empty()):
        print('No copied paths to paste')
        quit()
    else:
        paste_path = top()
        print(paste_path)

    exec_cmd('cp ' + paste_path + ' ./')

if __name__ == '__main__':
    main()
