#!/usr/bin/env python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments

import zipfile
import os


def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # make sure the folder is absolute

    # Figure out the filename this code should be based on
    # what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    # TODO: Create the zip file
    # TODO: Walk the entire folder tree and compress the files in each folder.
    print("Done.")


    backupToZip('/home/soeren/Documents/Fachbuecher')
