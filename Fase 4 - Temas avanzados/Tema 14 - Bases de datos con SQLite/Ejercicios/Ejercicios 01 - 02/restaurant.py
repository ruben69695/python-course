import sqlite3
from os import system
from time import sleep

database_name = "restaurante.db"

def print_main_menu():
    print("Welcome to the food menu program")
    print("================================")
    print("\t1 - Add a new category")
    print("\t2 - Add a new plate")
    print("\t3 - Show food menu")
    print("\n\tTo Exit: Type Exit")

def show_food_menu():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM category")
    categories = cursor.fetchall()
    print("\t======================")
    print("\t** Super Food Menu **")
    print("\t======================\n")
    print("\tThe Day Menu \t")
    for category in categories:
        category_id = category[0]
        category_name = category[1]
        print("\n\t{}:".format(category_name))
        cursor.execute("SELECT * FROM plate WHERE category_id = {}".format(category_id))
        plates = cursor.fetchall()
        for plate in plates:
            plate_name = plate[1]
            print("\t{}".format(plate_name))



def add_plate():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    show_categories()
    category_number = int(input("Please, choose the number of the category: "))
    plate_name = input("Please, write the name of the new plate: ")
    if plate_name != "":
        try:
            if plate_exists(plate_name):
                print("Error, this plate already exists")
            else:
                cursor.execute("INSERT INTO plate VALUES (NULL, '{}', {})".format(plate_name, category_number))
                connection.commit()
                print("The plate with name {} has been added succesfully".format(plate_name))
        except sqlite3.IntegrityError:
            print("Error, the plate name already exists or the category doesn't exists")
        finally:
            connection.close()
    else:
        print("The plate name can't be empty")

def plate_exists(name):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plate WHERE name = '{}'".format(name))
    plates = cursor.fetchall()
    num_plates = len(plates)
    if num_plates == 1:
        return True
    else:
        return False
    connection.close()

def show_categories():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM category")
    categories = cursor.fetchall()
    for category in categories:
        print("{} - {}".format(category[0], category[1]))

def add_category():
    name = input("Please, write the category name: ")
    try:
        #   Create the connection and the database and get the cursor
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        #   Insert the category in the table
        cursor.execute("INSERT INTO category VALUES (NULL, '{}')".format(name))
        connection.commit()
        print("This category {} has been added succesfully".format(name))
    except sqlite3.IntegrityError:
        print("This category {} already exists in the database, try another one".format(name))
    finally:
        connection.close()

def crear_db():
    #   Create the connection and the database and get the cursor
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    try:
        #   Table category
        cursor.execute('''
            CREATE TABLE category (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) UNIQUE NOT NULL
            )
        ''')
        #   Table plate
        cursor.execute('''
            CREATE TABLE plate (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) UNIQUE NOT NULL,
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES category(id)
            )
        ''')
        connection.commit()
    except sqlite3.OperationalError:
        print("The tables already exists")
    finally:
        connection.close()

#   Call to the function, to create the database and the tables
crear_db()

#   Main menu for the console application
while(True):
    system("clear")
    print_main_menu()
    op = input("\nPlease choose an operation: ")
    if op == "1":
        add_category()
        sleep(2.5)
    elif op == "2":
        add_plate()
        sleep(2.5)
    elif op == "3":
        show_food_menu()
        sleep(10)
    elif ((op == "exit") or (op == "Exit") or (op == "EXIT")):
        break # Exit the loop
    