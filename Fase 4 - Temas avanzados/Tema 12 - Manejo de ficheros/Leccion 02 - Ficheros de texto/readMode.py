from io import open

# Open a file in read mode and save all the text into a variable and prints the content of the file, close the file
file = open("fileToWrite.txt", "r")
text = file.read()
print(text)
file.close()

print("========= PROGRAM SEPARATOR ==========\n")

# Open a file in read mode and save all the lines into a lists, one line in the file is one element in the list
file = open("fileToWrite.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
file.close()

# IMPORTANT TIP -> If the file does not exists and you've opened in read mode, the program is going to crash!!!

# Open a file in read mode and situate the pointer in the character 10 in the file and read
print("========= PROGRAM SEPARATOR ==========\n")
file = open("fileToWrite.txt", "r")
file.seek(10)
text = file.read()
print(text)

# Now situate the pointer at the begin of the file and read
file.seek(0)
text = file.read()
print(text)
file.close()