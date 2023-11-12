# Assign 10 (binary for 2) to types of people.
types_of_people = 10
# Set x to a string with types of people interpolated.
x = f"There are {types_of_people} types of people."

# Set variable binary to be interpolated later.
binary = "binary"
# Set variable to be interpolated later.
do_not = "don't"
# Set y to string with interpolated variables.
y = f"Those who know {binary} and those who {do_not}."

# Print string x
print(x)
# Print string y
print(y)

# Print string with x interpolated.
print(f"I said: {x}")
# print string with y interpolated.
print(f"I also said: '{y}'")

# Set variable to boolean false
hilarious = False
# Set variable to string with an empty place holder.
joke_evaluation = "Isn't that joke so funny?! {}"
# Use format to interpolate variable into string with place holder
print(joke_evaluation.format(hilarious))

# Set a string
w = "This is the left side of..."
# Set another string
e = "a string with a right side."
# Print out string of concatenated w and e strings.
print(w + e)
