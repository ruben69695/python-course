from tkinter import *

root = Tk()
root.title("Hello World!")

menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=root.quit)

editMenu = Menu(menubar, tearoff=0)
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

helpMenu = Menu(menubar, tearoff=0)
helpMenu.add_command(label="Welcome")
helpMenu.add_command(label="About me...")

menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_cascade(label="Edit", menu=editMenu)
menubar.add_cascade(label="Help", menu=helpMenu)

# At the bottom of the script always
root.mainloop()