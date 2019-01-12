from tkinter import *

def seleccionar():
    cadena = ""

    if(leche.get()):
        cadena = "With milk"
    else:
        cadena = "Without milk"
    
    if(azucar.get()):
        cadena += " and with sugar"
    else:
        cadena += " and without sugar"

    monitor.config(text=cadena)

root = Tk()
root.title("Milk Bar")
root.config(bd=15)

azucar = BooleanVar()
leche = BooleanVar()

img = PhotoImage(file="imagen.gif")
Label(root, image=img).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="How do you want the coffee?").pack(anchor="w")
Checkbutton(frame, text="With Milk", variable=leche, onvalue=True, offvalue=False, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="With Sugar", variable=azucar, onvalue=True, offvalue=False, command=seleccionar).pack(anchor="w")

monitor = Label(frame, text="")
monitor.pack(anchor="w")

# At the bottom of the script always
root.mainloop()