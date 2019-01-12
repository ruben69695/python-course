import sqlite3

#   Create the connection to the database, if not exists it creates the db file for us
connection = sqlite3.connect("example.db")

#   Get the cursor of the connection, this objects allows us to execute sql sentences 
#   like create tables, select data, insert... etc
cursor = connection.cursor()

#   Create table
#cursor.execute("CREATE TABLE users (name VARCHAR(100), age INTEGER, email VARCHAR(100))")

#   Insert data
#cursor.execute("INSERT INTO users VALUES ('Ruben',22,'ruben.arre6@gmail.com')")

#   Select data from the table
cursor.execute("SELECT * FROM users")

#   Get only one item of the data from the select, after this fetch the cursor is at the next 
#   row of the selected data until we execute another sql select sentence
user = cursor.fetchone()
print(user)

#   Insert massive data
users = [
    ("Paco", 34, "paco@example.es"),
    ("Spike", 24, "spike@example.es"),
    ("Frank", 67, "frank@example.com")
]
cursor.executemany("INSERT INTO users VALUES (?,?,?)", users)

#   Select all the data
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

for tmp in users:
    print(tmp[0],", edad:",tmp[1])

# When you execute commands that changes the database you need to commit the commands
connection.commit()
connection.close()