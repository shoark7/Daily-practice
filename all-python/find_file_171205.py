"""Find file or directory of given name in a directory

    In Unix, there's a CLI program named 'find'.
    This program prints absolute paths of files with names matching user input \
    in a given directory.

    My goal is to extend Unix's find program to platform independent program.

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


parser = argparse.ArgumentParser(description="Arg parser for find program")
parser.add_argument('path', nargs='?', default='.', help="Path to be searched. Defaults to current\
                    directory")
parser.add_argument('-type', choices=['a', 'd', 'f'], default='a', dest="type",
                    help="Type of the file wanted")
parser.add_argument('-name', required=True, dest='name', help="Name of the file wanted")

args = parser.parse_args()


if not os.path.exists(args.path):
    raise OSError("Invalid or relative path is given")


pattern = re.compile(args.name)


def find_specific_file(root, file_list):
    for file in file_list:
        if pattern.search(file):
            print(os.path.join(root, file))


for root, dirs, files in os.walk(args.path):
    if args.type == 'f':
        find_specific_file(root, files)
    elif args.type == 'd':
        find_specific_file(root, dirs)
    else:
        find_specific_file(root, dirs + files)
