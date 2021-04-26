from sys import argv
#execute script with arguement (filename) passed into it
script, filename = argv
#opens (filename) and returns it as an object into (txt)
txt = open(filename)
#prints string with (filename) arguement from earlier
print(f"Here's your file {filename}:")
#runs read command on (txt) object to
#return the entire object then prints to screen
print(txt.read())
#close (txt) object
txt.close()
#user prompt
print("Type the filename again:")
#takes user input into (file_again) and also changed the prompt to (> )
file_again = input("> ")
#opens (file_again) from earlier input and returns it as an object (txt_again)
txt_again = open(file_again)
#runs read command on (txt_again) object to
#return the entire object then prints to screen
print(txt_again.read())
#close the (txt_again) object
txt_again.close()
