numbers = []

def list_num(max, step):
    i = 0
    x = int(max)
    s = int(step)
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + s
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

def list_num_for(max, step):
    i = 0
    x = int(max)
    s = int(step)
    for i in range(1, x, s):
        print(f"At the top i is {i}")
        numbers.append(i)

        #i = i + s
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

high = input("Enter a number to count to: ")
increment = input("Enter a number to increment the count: ")
#list_num(high, increment)
list_num_for(high, increment)

print("The numbers: ")

for num in numbers:
    print(num)
