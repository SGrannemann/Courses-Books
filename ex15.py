# import argv module
from sys import argv
# define the variables and their order inside argv (argv == Arguments passed via commandline)
script, filename = argv
# open filename (which is an argument passed via commandline) and assign that file object to a variable called txt
txt = open(filename)
#simple formatted print
print(f"Here's your file {filename}:")
# Printing of the return of a function of an file object
print(txt.read())

txt.close()
#print("Type the filename again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())
