from tkinter import *

root = Tk()
root.title("Hello World!")
root.resizable(1,1)

'''
text = StringVar()
text.set("Don't kill me amigoo!")

Label(root, text="First label").pack(anchor="nw")
label = Label(root, text="Hello World!")
label.pack(anchor="center")
Label(root, text="Last label").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana", 20))
label.config(textvariable=text)
'''

image = PhotoImage(file="imagen.gif")
Label(root, image=image, bd=0).pack(side="left")


# At the bottom of the script always
root.mainloop()