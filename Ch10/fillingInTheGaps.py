#!/usr/bin/env python3
# fillingInTheGaps.py - finds all files with a given prefix in a folder
# locates gaps in the numbering of files and renames files to fill the gaps.


import os
import re
import shutil
from pathlib import Path



def fillGaps(folder, prefix, extension):
    home = str(Path.home())
    folder = os.path.abspath(home + folder)
    # test code that creates 100 files with only even numbering:
    # for i in range(0, 100, 2):
    #     count = i
    #     filepath = folder + '/' + f'{prefix}{count}.txt'
    #     file = open(filepath, 'w')
    #     file.close()

    # create a regex based on the prefix specified. must contain numbers afterwards
    # zeros will be ignored.
    regex = r'({0})(\d+)'.format(prefix)
    regExObject = re.compile(regex)

    index = 0
    # only look through files in the dir if correct extension
    # sort the files to find gaps via an incremented counter
    for file in sorted(Path(folder).glob(f'*.{extension}')):
        # TODO: make the iterable sorted by integer index (now: 10 comes before 2)
        mo = regExObject.search(os.path.basename(file))
        if mo: # ignore any files with the correct extension but wrong prefix
            if int(mo.group(2)) != index: # evaluates to true if there is a gap

                new_name = re.sub(r'\d+', str(index), os.path.basename(file))
                new_name_folder = folder + '/' + new_name
                print(f'renaming {file}')
                print(f'new name: {new_name_folder}')

                shutil.move(file, new_name_folder)

                
            index += 1






###############################################################################
input_specify = 'Specify the {}. \n'
folder = input(input_specify.format('folder'))
prefix = input(input_specify.format('prefix of the files'))
extension = input(input_specify.format('extension of the files'))

fillGaps(folder, prefix, extension)
