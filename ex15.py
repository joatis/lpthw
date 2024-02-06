# inport the argv from sys to get arguments.
from sys import argv
# unpack argv into two variables.
script, filename = argv
# open the filename in argv as a text file
txt = open(filename)
# print the filename and the files contents after reading
print(f"Here is your file {filename}:")
print(txt.read())
# Prompt the user to re-enter the filename
print("Type the filename again:")
file_again = input("> ")
# Open another file handle.
txt_again = open(file_again)
# print the contents of the file from the new filehandle.
print(txt_again.read())
