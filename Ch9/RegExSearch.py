from pathlib import Path
import re


path_to_search = input('Which path to search?\n')
pathObject = Path(path_to_search)

regex = input('Which RegEx to match?\n')
regExObject = re.compile(regex)

for file in pathObject.glob('*.txt'):
    fileObject = open(file, 'r')
    contents = fileObject.read()

    for match in regExObject.findall(contents):
        print('Match found:', file, match)
