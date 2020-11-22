#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current working directory.

import csv
from pathlib import Path
pathToCSVs = Path.cwd() / Path('Ch16')
pathForFilesWithoutHeader = pathToCSVs / Path('headerRemoved')
if not pathForFilesWithoutHeader.exists():
    pathForFilesWithoutHeader.mkdir()

# Loop through every csv file
for csvFile in pathToCSVs.glob('*.csv'):
    print('Removing header from ' + str(csvFile) + '...')

    # Read the CSV file in (skipping first row)
    
    with open(csvFile) as csvFileObj: 
        readerObj = csv.reader(csvFileObj)
        csvRows = [row for row in readerObj if readerObj.line_num != 1]
    
    # Write out the CSV file
    csvFileObj = open(pathForFilesWithoutHeader / csvFile.name, 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

