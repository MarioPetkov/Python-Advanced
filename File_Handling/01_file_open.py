import os

file_name = "text.txt"

try:
    file = open(file_name)
    print("File found")
except FileNotFoundError:
    print("File is not found")


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())