from tkinter import *

root = Tk()
root.title("Hello World!")

text = Text(root)
text.pack()
text.config(width=30, height=10, font=("Verdana", 12), padx=5, pady=5, selectbackground="red")

# At the bottom of the script always
root.mainloop()