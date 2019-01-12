from tkinter import *

root = Tk()
root.title("Entries")

# Entry for the Name
lblName = Label(root, text="Name:")
lblName.grid(row=0, column=0, sticky="w", padx=5, pady=5)

nameEntry = Entry(root)
nameEntry.grid(row=0, column=1, padx=5, pady=5)
nameEntry.config(justify="left", state="normal")

# Entry for the lastname
lblLastName = Label(root, text="LastName:")
lblLastName.grid(row=1, column=0, sticky="w", padx=5, pady=5)

lastNameEntry = Entry(root)
lastNameEntry.grid(row=1, column=1, padx=5, pady=5)
lastNameEntry.config(justify="right", state="normal")

# At the bottom of the script always
root.mainloop()