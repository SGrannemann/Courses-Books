#! python3


# The bulletPointAdder.py script gets the text from the clipboard,
# add a star and space to the beginning of each line,
# and then paste this new text to the clipboard.



import pyperclip
text = pyperclip.paste()


# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): #loop through the list of lines
    lines[i] = '* ' + lines[i] #add star to each string in list
text = '\n'.join(lines)



pyperclip.copy(text)
