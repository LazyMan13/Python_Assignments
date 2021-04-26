from random import randrange
#set function with two inputs with variables named between ()
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #takes function variables set above to use
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def math(intOne, operator, intTwo):
    if operator == 1:
        total = intOne + intTwo
        print(f"{intOne} + {intTwo} is {total}")
    elif operator == 2:
        total = intOne - intTwo
        print(f"{intOne} - {intTwo} is {total}")
    elif operator == 3:
        total = intOne / intTwo
        print(f"{intOne} / {intTwo} is {total}")
    elif operator == 4:
        total = intOne * intTwo
        print(f"{intOne} * {intTwo} is {total}")
    elif operator == 5:
        total = intOne % intTwo
        print(f"{intOne} mod {intTwo} is {total}")
    elif operator == 6:
        total = (float(intOne)/100) * float(intTwo)
        print(f"{intOne}% of {intTwo} is {total}")
    elif operator == 7:
        if intTwo == 0:
            print("Having 0 does not make sense here.")
            return
        else:
            total = float(intOne)/float(intTwo) * 100.0
            print(f"{intOne} is {total}% of {intTwo}")
    else:
        print("Operator not valid for this function.")


print("We can just give the function numbers directly:")
#calls function passing 20 & 30 into it
cheese_and_crackers(20,30)


print("OR, we can use variables from our script:")
#sets variables in script
amount_of_cheese = 10
amount_of_crackers = 50
#calls function passing the variables to it
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
#calls function passing the total of the integers
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
#calls function passing the total of the math adding variables and ints
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

for i in range(1,8):
    counter = 0
    randNums = []
    x = range(2)
    for counter in x:
        randNums.append(randrange(1,100))
    math(randNums[0], i, randNums[1])

math1 = 20
math2 = 40
math(50,4,75)
math(math1,7,math2)
math(math1+10,2+1,math2*4)
