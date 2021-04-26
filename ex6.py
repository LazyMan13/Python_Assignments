#setting value to 10
types_of_people = 10
#displaying variable as 10 in the string
x = f"There are {types_of_people} types of people."

#setting variable to string "binary"
binary = "binary"
#setting variable to string "don't"
do_not = "don't"
#setting a string with variable strings inside string
y = f"Those who know {binary} and those who {do_not}."

#printing the two longer strings from earlier
print(x)
print(y)

#printing a string with other strings from earlier embedded inside it
print(f"I said: {x}")
print(f"I also said: '{y}'")

#setting variable boolean value to false
hilarious = False
#setting string with empty placeholder
joke_evaluation = "Isn't that joke so funny?! {}"

#printing string defined in joke_evaluation and formatting it to
#place the boolean variable  from earlier inside the empty placeholder
print(joke_evaluation.format(hilarious))

#setting strings to simple variables
w = "This is the left side of..."
e = "a string with a right side."

#displaying both strings by combining them with the + sign
print(w + e)
