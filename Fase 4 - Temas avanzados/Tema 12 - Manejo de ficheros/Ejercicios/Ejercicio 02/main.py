from io import open
from sys import argv

fileName = "contador.txt"
arguments = argv
line = ""
number = 0

try:
    file = open(fileName, "r+")
except FileNotFoundError as e:
    print("File contador.txt not found, let's create it")
    file = open(fileName, "w+")
    file.write("0")
    file.seek(0)

if (file != None):
    line = file.readline()
    if (line != ""):
        number = int(line)
        if (len(arguments) > 1):
            file.seek(0)
            if (arguments[1] == "inc"):
                number += 1
                file.write(str(number))
            elif (arguments[1] == "dec"):
                number -= 1
                file.write(str(number))
        print(number)
    else:
        print("Error the file is empty, let's create the 0 value on it")
        file.seek(0)
        file.write("0")
    file.close()



