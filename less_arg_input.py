from sys import argv
#read the WYSS section for how to run this
script, conversionFactor, heightInches = argv
conversion = float(conversionFactor)
height = float(heightInches)
print("The script is called:", script)
weight = float(input("How much do you weigh in pounds? "))
BMI = (weight*conversion)/(height*height)

print(f"You weight {weight}.")
print(f"You are {height} inches tall.")
print(f"Using a conversion factor of {conversion}, your BMI is {BMI}.")
