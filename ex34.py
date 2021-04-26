from natural import number

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
language = ['Python', 'Java', 'C++', 'LUA', 'Visual Basic']

print(animals)
print()

print("The animal at 1. ", animals[1])
print("The 3rd animal. ", animals[3-1])
print("The 1st animal. ", animals[1-1])
print("The animal at 3. ", animals[3])
print("The 5th animal. ", animals[5-1])
print("The animal at 2 ", animals[2])
print("The 6th animal. ", animals [6-1])
print("The animal at 4. ", animals[4])
print()

for i in range(len(animals)):
    print("The %s animal is at %d and is a %s." % (number.ordinal(i+1), i, animals[i]))
    print("The animal at %d is the %s animal and is a %s." % (i, number.ordinal(i+1), animals[i]))
    print()

print("\n", language, "\n")

for i in range(len(language)):
    print("The %s language is at %d and is %s." % (number.ordinal(i+1), i, language[i]))
    print("The language at %d is the %s language and is %s." % (i, number.ordinal(i+1), language[i]))
    print()
