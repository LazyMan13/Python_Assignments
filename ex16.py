from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#stalls at prompt to allow user to choose to quit
input("?")

print("Opening the file.")
#opens file with write mode, sets to target object
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
#truncate with no size specified, so current file stream position
#this will erase the contents of the file
target.truncate()

#print("Now I'm going to ask you for three lines.")
##set 3 lines to user's input
#line1 = input("line 1: ")
#line2 = input("line 2: ")
#line3 = input("line 3: ")

#use split command to input multiline into list object for later
list = input("Now I'm going to ask you for three lines, seperated by a comma(,)").split(",")

print("I'm going to write these to the file.")
##write the earlier lines to the target object
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#join list object from earlier and attack newline escape
#write result to target
target.write('\n'.join(list))

print("And finally, we close it.")
#close the target object
target.close()
