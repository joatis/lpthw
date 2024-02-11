# import argv from sys
from sys import argv

# unpack argv
script, input_file = argv

# print the whole input file, arg is a file object
def print_all(f):
  # print the results of the file read method
  print(f.read())

# Set the "read head" back to begining of file
def rewind(f):
  # call the file objects seek method to position the head
  f.seek(0)

# a function prints the line of a specified line inb a file object
def print_a_line(line_count, f):
  # prints line position the result of the file objects readline
  print(line_count, f.readline(), end="")

# Open the input file and assign to variable
current_file = open(input_file)

# Print intro
print("First let's print the whole file:\n")

# calls the function that uses the file object to print the whole contents
print_all(current_file)

# Informs that the head is being rewound
print("Now let's rewind, kind of like a tape.")

# A function that resets the file head back to beginning using the file object as arg
rewind(current_file)

# Informational text
print("Let's print three lines:")

# Inititialize current_line to 1
current_line = 1
# calling function that will print current_line of specified file
print_a_line(current_line, current_file)

# increment current_line by 1
current_line += 1
# print a line with new value
print_a_line(current_line, current_file)

# increment current_line by 1
current_line += 1 
# print a line with new value
print_a_line(current_line, current_file)
