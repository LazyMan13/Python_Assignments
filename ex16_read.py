from sys import argv
script, filename = argv
txt = open(filename)
print(f"Presenting {filename}:")
print(txt.read())
txt.close()
