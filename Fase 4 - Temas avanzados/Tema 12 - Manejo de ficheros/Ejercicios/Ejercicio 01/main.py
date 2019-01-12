from io import open

persons = []

file = open("personas.txt", "r", encoding="utf8")
lines = file.readlines()

for line in lines:
    elements = line.split(";")
    persons.append (
        {"id": elements[0], "name": elements[1], "lastName": elements[2], "birthDate": elements[3]}
    )

for person in persons:
    print("ID {} -> My name is {} {} and my birtdate is {}".format(person["id"], person["name"], person["lastName"], person["birthDate"]))
