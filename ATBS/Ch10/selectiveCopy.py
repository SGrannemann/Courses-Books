#!/usr/bin/env python3
# selectiveCopy.py - Copies all files in a specified foler with a specified
# extension to another folder

# input: folder and extension. use glob pattern to find all files in folder
# move them to a different folder as specified
import os
from pathlib import Path
import shutil


def selectivecopy(folder, extension, destination):
    folder = os.path.abspath(folder)
    destination = os.path.abspath(destination)
    print(destination)
    if not os.path.exists(destination):
        Path(destination).mkdir()
    for foldername, subfolders, filenames in os.walk(folder):
        for file in Path(foldername).glob(f'{extension}'):
            shutil.copy(file, destination)


folder = input('Which folder shall be searched?')
extension = input('Specify the extension of files that shall be moved.')
destination = input('Specify the destination directory.')
selectivecopy(folder, extension, destination)
