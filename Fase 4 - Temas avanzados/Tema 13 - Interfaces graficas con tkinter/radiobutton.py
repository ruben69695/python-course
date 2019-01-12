from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def limpiar():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
root.title("Hello World!")

opcion = IntVar()

Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(root, text="")
monitor.pack()

Button(root, text="Reset", command=limpiar).pack()

# At the bottom of the script always
root.mainloop()