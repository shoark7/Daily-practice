"""Find file or directory of given name in a directory

    In Unix, there's a CLI program named 'find'.
    This program prints absolute paths of files with names matching user input \
    in a given directory.

    'Everything is a file in Unix'. We know that.
    So unlike title of this module, you can filter out file or directory or even all in this
    program.

    I'll update this program continuously like regular expression matching.

    Start Date : 2017/12/05
"""
import argparse
import os
import os.path
import re


# All variables will be given by input later.
path = os.getcwd()
file_type = 'file'
name = '.py'


if not os.path.exists(path):
    raise OSError("Invalid or relative path is given")

for root, dirs, files in os.walk(path):

    if file_type == 'file':
        for file in files:
            if name in file:
                print(os.path.join(root, file))
    elif file_type == 'dir':
        for dir in dirs:
            if name in dir:
                print(os.path.join(root, dir))
    else:
        for file in files:
            if name in file:
                print(os.path.join(root, file))
        for dir in dirs:
            if name in dir:
                print(os.path.join(root, dir))
