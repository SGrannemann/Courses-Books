#!/usr/bin/env python3
# mbc.pyw - Saves and loads pieces of text to the clipboard.
# Usage: python3 mcb.pyw save <keyword> - Saves the clipboard to the keyword
#        python3 mcb.pyw <keyword> - Loads keyword to the clipboard
#        python3 mcb.pyw list - Loads all keywords to the clipboard
#        python3 mcb.pyw delete <keyword> - Deletes a keyword
#        python3 mcb.pyw delete - Deletes all keywords

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(mcbShelf.keys()))
    elif sys.argv[1].lower() == 'delete':
        for keyword in list(mcbShelf.keys()):
            del mcbShelf[keyword]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
