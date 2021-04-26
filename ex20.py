from sys import argv

script, input_file = argv
#function that reads whole file then prints out
def print_all(f):
    print(f.read())
#function that returns location in file to beginning
def rewind(f):
    f.seek(0)
#function that reads a file's line location and prints
def print_a_line(line_count, f):
    print(line_count, f.readline())
#opens input_file into current_file
current_file = open(input_file)

print("First let's print the whole file:\n")
#calls print_all with current_file as argument
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
#calls rewind with current_file as argument
rewind(current_file)

print("Let's print three lines:")
#sets current_line to line 1
current_line = 1
#calls print_a_line with arguments of current_line and current_file
print_a_line(current_line, current_file) #current_line = 1
#1 is passed to print_a_line function argument which accepts it as line_count parameter so line_count = 1
#increments current_line by 1 and runs function as before
current_line += 1
print_a_line(current_line, current_file) #current_line = 2
#2 is passed to print_a_line function argument which accepts it as line_count parameter so line_count = 2
#increments current_line by 1 and runs function as before
current_line += 1 
print_a_line(current_line, current_file) #current_line = 3
#3 is passed to print_a_line function argument which accepts it as line_count parameter so line_count = 3
