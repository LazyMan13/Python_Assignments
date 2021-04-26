print("I will now count my chickens:")

#Divide 30 by 6, then add 25 to the result
print("Hens", 25.0 + 30.0 / 6.0)
#Multiply 75 and 3, take the result divide by 4 and use the remainder
#(modulo) of result to subtract from 100
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

#4 modulo 2 result 0, 1 divided by 4 result .25
#3 + 2 = 5 + 1 = 6 - 5 = 1
#1 + 0 = 1 - .25 = .75 + 6 = 6.75
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")

#3 + 2 = 5
#5 - 7 = -2
#5 < -2 is False
print(3.0 + 2.0 < 5.0 - 7.0)

#explained above
print("What is 3 + 2?", 3.0 + 2.0)
#explained above
print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")

#5 is greater than -2 so True
print("Is it greater?", 5.0 > -2.0)
#5 is greater than or equal to -2 so True
print("Is it greater or equal?", 5.0 >= -2.0)
#5 is not less than or equal to -2 so False
print("Is it less or equal?", 5.0 <= -2.0)
