from tkinter import *

def sumar():
    r.set( float(n1.get()) + float(n2.get()) )

def restar():
    r.set( float(n1.get()) - float(n2.get()) )

def producto():
    r.set( float(n1.get()) * float(n2.get()) )

def limpiar():
    n1.set("")
    n2.set("")
    r.set("")

root = Tk()
root.title("Calculator")
root.config(padx=10, pady=10)
root.resizable(0,0)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Number 1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root, text="Number 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Result").pack()
Entry(root, state="disabled", textvariable=r, justify="center").pack()

Label(root, text="").pack()
Button(root, text="Sum", command=sumar).pack(side="left", anchor="nw")
Button(root, text="Subtract", command=restar).pack(side="left")
Button(root, text="Multiply", command=producto).pack(side="left")
Button(root, text="Clean", command=limpiar).pack(side="left")



# At the bottom of the script always
root.mainloop()