from tkinter import Tk, Menu, Text, StringVar, Label
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open

file_route = "" # To save the opened file route

def new():
    global file_route
    print("The file: " + file_route)
    if file_route != "":
        result = MessageBox.askyesno("Prevent data loss","Do you want to save the file before create a new file?")
        if result:
            save()
    edit_box.delete(1.0, "end")  
    file_route = ""
    monitor_message.set("New file created")  

def openfile():
    global file_route
    file = FileDialog.askopenfile("r", 
        initialdir=".", 
        filetypes=(("Text files", "*.txt"),), 
        title="Open a file text")
    if file is not None:
        print(file)
        edit_box.delete(1.0, "end")
        content = file.read()
        edit_box.insert("insert", content)
        file.close()
        file_route = file.name
        root.title = "{} - Super Editor".format(file.name)

def save():
    global file_route
    if file_route != "":
        file = open(file_route, "w", encoding="utf8")
        file.write(edit_box.get(1.0, "end-1c"))
        file.close()
        monitor_message.set("File saved correctly")
    else:
        save_as()
    
def save_as():
    global file_route
    file = FileDialog.asksaveasfile("w", title="Save File As...", defaultextension=".txt")
    if file is not None:
        file_route = file.name
        file.write(edit_box.get(1.0, "end-1c"))
        file.close()
        monitor_message.set("File saved correctly as {}".format(file.name.split("/")[-1]))
    else:
        monitor_message.set("File saved canceled")

# Form root
root = Tk()
root.title = "Super Editor"

# Main menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As...", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")
root.config(menu=menubar)

# Main edit box
edit_box = Text(root)
edit_box.pack(fill="both", expand=1)
edit_box.config(bd=0, padx=10, pady=5, font=("Monaco", 12))

# Bottom monitor
monitor_message = StringVar()
monitor_message.set("Welcome to the Super Editor developed in Python")
label_monitor = Label(root, textvar=monitor_message, justify="left")
label_monitor.pack(side="left")


# Finalmente bucle de la apliación
root.mainloop()