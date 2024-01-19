# Print a string
print("Mary had a little lamb.")
# Print a string that uses the format string method to interpolate.
print("Its fleece was white as {}".format('snow'))
# Print a string
print("And everywhere that Mary went.")
# Print a charater 10 times
print("." * 10) # what'd it do?

# assign each variable a character value.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# The second arg is a key word param called end. Usually it defaults to a 
# \n but here we are overriding it with a space that causes both print statements
# to be written on the same line.
# Print the concatented values using 2 separate print statements.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
