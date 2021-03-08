#!/usr/bin/env python

import os


THIS_PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FILE = THIS_PARENT_DIR + '/copy-stack.txt'

def push(copy_path):
    f = open(SAVE_FILE, 'a')
    f.write(os.path.abspath(copy_path) + '\n')
    f.close()

def top():
    f = open(SAVE_FILE, 'r')
    stack = f.read()
    f.close()

    stack = stack.split('\n')
    return stack[-2]

def pop():
    f = open(SAVE_FILE, 'r')
    stack = f.read()
    f.close()

    stack = stack.split('\n')
    element = stack[-2]
    stack = '\n'.join(stack[:-2])
        
    f = open(SAVE_FILE, 'w+')
    for line in stack:
        f.write(line)
    f.write('\n')
    f.close()

    return element

def s_len():
    f = open(SAVE_FILE, 'r')
    stack = f.read().split('\n')
    f.close()
    return len(stack) - 1

def is_empty():
    return s_len() <= 1
