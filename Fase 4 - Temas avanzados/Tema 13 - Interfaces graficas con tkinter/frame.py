from tkinter import *

root = Tk()
root.title("Hello World!")
root.resizable(1,1)

# Configuración de un marco
frame = Frame(root, width=480, height=320)
frame.pack(fill="both", expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="yellow")
root.config(bd=15)
root.config(relief="ridge")

# At the bottom of the script always
root.mainloop()