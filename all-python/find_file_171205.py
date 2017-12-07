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
    Last update date: 2017/12/07
"""
import argparse
import os
import os.path
import re


__version__ = '1.0.0'


parser = argparse.ArgumentParser(description="Arg parser for find program")
parser.add_argument('path', nargs='?', default='.',
                    help="Path to be searched. Defaults to current directory")
parser.add_argument('-type', choices=['a', 'd', 'f'], default='a', dest="type",
                    help="Type of the file wanted")
parser.add_argument('-name', required=True, dest='name', help="Name of the file wanted")
parser.add_argument('-abs-path', action='store_const', const=True, dest="abs_path", default=False,
                    help="Whether or not to print out absolute path")
args = parser.parse_args()


def scan_dir_and_file(root, file_list):
    root = os.path.join(os.path.abspath(root)) if args.abs_path else root
    for file in file_list:
        if pattern.search(file):
            print(os.path.join(root, file))


if not os.path.exists(args.path):
    raise OSError("Invalid or relative path is given")

pattern = re.compile(args.name)


for root, dirs, files in os.walk(args.path):
    if args.type == 'f':
        scan_dir_and_file(root, files)
    elif args.type == 'd':
        scan_dir_and_file(root, dirs)
    else:
        scan_dir_and_file(root, dirs + files)
