name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
#for the sake of decimal points i'm using the round function
#given in the text for cm and kgs, but if taken
#out it would be more precise, it would really depend on how
#accurate we are going for here.
weightMetric = round(weight * 0.45359237)
heightMetric = round(height * 2.54)

print(f"Let's talk about {name}.")
print(f"He's {height} inches, or {heightMetric} cm tall.")
print(f"He's {weight} pounds, or {weightMetric} kgs heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
