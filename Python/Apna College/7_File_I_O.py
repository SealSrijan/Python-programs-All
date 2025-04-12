#Bhai, ki jinis dekhe nilm.... Python e puro onno file read korte parbe... :)
#dekha jaak, kmn hoe byapar ta.. 
file = open("demo.txt","r")
print(file.read())
file.close()

file = open("demo.txt", "w") #"w" overwrites the existing data in the file
file.write("Srijan")
file.close()

file = open("demo.txt", "r+")
file.write(" Srijan Seal")
print(file.read())
file.close()

file = open("names.docx", "a+")
file.write("\n4. Sanjit Kumar Saha")
print(file.read())
file.close()

# "r+" : read + overwrite (ptr starting, i.e., starts overwriting from beginning, no truncate(format))
# "w+" :  "         "     (no concept of pointer, because file is truncated)
# "a+" : read + append    (pointer at end, no truncate)

# modified style of writing, using 'with'

with open("names.docx", "r") as f:
    print(f.read())

#for deleting a file, we need to use a module
import os
os.remove("demo.txt")

# Practice Set
f = open("python.txt", "w")
f.write("Hi everyone.\nWe are learning file I/O.\nusing Java.\nI like programming in Java")
f.close()

f = open("Python.txt", "r")
data = f.read()
f = open("Python.txt", "w")
f.write(data.replace("Java", "Python"))
print(data.find("learning"))


#end of lecture 7(50:48)