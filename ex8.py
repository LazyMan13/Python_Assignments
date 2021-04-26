# set variable with 4 empty placeholders
formatter = "{} {} {} {}"

# formatting 4 ints to placeholers in variable
print(formatter.format(1, 2, 3, 4))
# formatting 4 strings to placeholers in variable
print(formatter.format("one", "two", "three", "four"))
# formatting 4 boolean to placeholers in variable
print(formatter.format(True, False, False, True))
# formatting to call the variable as a string to placeholers in the variable
print(formatter.format(formatter, formatter, formatter, formatter))
# formatting 4 more strings to the variable, now each is on it's own line
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
