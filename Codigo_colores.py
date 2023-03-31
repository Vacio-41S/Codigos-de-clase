from tkinter import *
from tkinter import filedialog as filedialog 
from tkinter import messagebox as MessageBox 
from tkinter import colorchooser as ColorChooser

root=Tk()
root.geometry("600x500")

def color():

    valorRGB=red.get()+blue.get()+green.get() 

    if len(valorRGB)>6:
     MessageBox.showwarning("Alerta","SON MAS DE 6 DIGITOS, SE ASIGNARA UN COLOR DEFAULT")
     root.config(bg="#000000")

    if len(valorRGB)<6:
     MessageBox.showwarning("Alerta","SON MENOS DE 6 DIGITOS, SE ASIGNARA UN COLOR DEFAULT")
     root.config(bg="#000000")

    if len(valorRGB)==6:
     root.config(bg=("#"+red.get()+blue.get()+green.get()))

red=StringVar()
Label(root, text="Rojo").pack()
Entry(root, justify="center", textvariable=red).pack()

blue=StringVar()
Label(root, text="Azul").pack()
Entry(root, justify="center", textvariable=blue).pack()

green=StringVar()
Label(root, text="Verde").pack()
Entry(root, justify="center", textvariable=green).pack()

Button(root, text="Set Color", command=color).pack()

root.mainloop()