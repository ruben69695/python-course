from io import open

# Create if not exists or overwrite if exists and put text inside the file, after all the ops with the file, close it!
text = "One line\nAntoher line\n"
file = open("fileToWrite.txt", "w")
file.write(text)
file.close()

