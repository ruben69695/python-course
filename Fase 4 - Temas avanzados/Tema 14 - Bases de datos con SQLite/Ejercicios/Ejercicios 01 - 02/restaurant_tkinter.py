from tkinter import *
from PIL import Image, ImageTk
import sqlite3

def get_categories():
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM category")
    categories = cursor.fetchall()
    connection.close()
    return categories

def get_plates_per_category(categoryId):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM plate WHERE category_id = {}".format(categoryId))
    plates = cursor.fetchall()
    connection.close()
    return plates

database_name = "restaurante.db"
root = Tk()
root.title("El barete de Python - Menú")
root.resizable(0,0)


imgFrame = Frame(root, padx=30, pady=30)
menuFrame = Frame(root, padx=30, pady=30)
menuSonFrame = Frame(menuFrame, padx=10, pady=10)
image = Image.open("food_cartoon.jpg")
image = image.resize((250, 250), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

Label(imgFrame, image=image).pack()
Label(menuFrame, text="EL BARETE DE PYTHON", font=("Lucida Grande", 22, "bold"), ).pack()
Label(menuSonFrame, text="Menú del día", font=("Lucida Grande", 18, "bold"), ).pack()

imgFrame.pack(side="left")
menuFrame.pack(side="right")
menuSonFrame.pack()

for category in get_categories():
    category_id = category[0]
    category_name = category[1]
    Label(menuSonFrame, text=category_name, font=("Lucida Grande", 16, "bold"), pady=20).pack()
    for plate in get_plates_per_category(category_id):
        plate_name = plate[1]
        Label(menuSonFrame, text=plate_name, font=("Lucida Grande", 16)).pack()

Label(menuFrame, pady=30, text="12€ (IVA inc.)", font=("Lucida Grande", 18, "bold"), ).pack(anchor="se")


root.mainloop()