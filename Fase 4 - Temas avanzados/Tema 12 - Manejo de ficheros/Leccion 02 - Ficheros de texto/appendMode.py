from io import open

# Open the file in append mode, if exists it opens the file and  if not exists it creates the file, when the append mode is
# called, the pointer in the file it's situated at the end to support adding new lines
text = "New line in append moden\n"
file = open("fileToWrite.txt", "a")
file.write(text)
file.close()

with open("fileToWrite.txt", "r") as file:
    for line in file:
        print(line)
file.close()