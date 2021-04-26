people = 30
cars = 40
trucks = 15

#print if more cars than people
if cars > people:
    print("We should take the cars.")
#print if less cars than people
elif cars < people:
    print("We should not take the cars.")
#print if nothing else is true above
else:
    print("We can't decide.")

#print if more trucks than cars
if trucks > cars:
    print("That's too many trucks.")
#print if less trucks than cars
elif trucks < cars:
    print("Maybe we could takee the trucks.")
#print if nothing else is true above
else:
    print("We still can't decide.")

#print if more people than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
#print if nothing else is true above
else:
    print("Fine, let's just stay home then.")

#print if more people than trucks and less people than cars
if (people > trucks) and (people < cars):
    print("There are less trucks than people, but more cars.")
#print if less people than trucks and less people than cars
elif (people < trucks) and (people < cars):
    print("There are more trucks and cars than people.")
#print if more people than trucks and more people than cars
elif (people > trucks) and (people > cars):
    print("There are less trucks and cars than people.")
#print if nothing else is true above
else:
    print("There are more trucks than people, but less cars.")
