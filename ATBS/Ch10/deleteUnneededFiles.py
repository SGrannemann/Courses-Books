#!/usr/bin/env python3
# deleteUnneededFiles.py - Prints absolute paths for files with a size you can specify

# input: folder and extension. use glob pattern to find all files in folder
# move them to a different folder as specified
import os


def deleteUnneededFiles(folder, size):
    folder = os.path.abspath(folder)
    for folders, subfolders, filenames in os.walk(folder):
        for file in filenames:
            if os.path.getsize(os.path.join(folders, file)) > size:
                print(os.path.join(folders, file))


folder = input('Which folder shall be searched?')
size = int(input('What size threshold?'))

deleteUnneededFiles(folder, size)
