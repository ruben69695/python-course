from io import open

# Use r+ to open a file if exists and write and read from the file
file = open("fileToWrite.txt", "r+")
lines = file.readlines()
lines[2] = "This line has been modified in memory, running the python script\n"
file.seek(0)
file.writelines(lines)
file.close()

# IMPORTANT TIP -> If the file does not exists and you've opened in read mode, the program is going to crash!!!