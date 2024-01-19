# init formatter with a braces to accept 4 args.
formatter = "{} {} {} {}"

# Print passing a call the format function of the string variable formatter passing 4 ints.
print(formatter.format(1,2,3,4))
# Print passing a call the format function of the string variable formatter passing 4 strings.
print(formatter.format("one", "two", "three", "four"))
# Print passing a call the format function of the string variable formatter passing 4 booleans that get converted to strings.
print(formatter.format(True, False, False, True))
# Print passing a call the format function of the string variable formatter passing itselef 4 times.
print(formatter.format(formatter, formatter, formatter, formatter))

# Print passing a call the format function of the string variable formatter passing 4 strings on separate lines.
print(formatter.format(
  "Try your",
  "Own test here",
  "Maybe a poem",
  "Or a song about fear"
))