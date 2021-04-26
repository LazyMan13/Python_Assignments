from sys import argv
from os.path import exists

script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output files exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)
#keeping indication of script completion
print("Alright, all done.")

out_file.close()
in_file.close()

#searched online to better represent a oneline
#rather than using semicolons a mile long
# "with" auto closes instead of using ".close()"
#the print("Finished") wasn't totally neccesary
#altho I felt it was better to show some indication
#that the file finished for the user

#with open( to_file, 'w') as fw, open(from_file) as fr: fw.write(fr.read()), print("Finished")
