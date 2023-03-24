from tkinter import *

def sumar():
    r.var = int(n1.get()) + int(n2.get())
        
def resta():
    r.var = int(n1.get()) - int(n2.get())
    
def producto():
    r.var = int(n1.get()) * int(n2.get())
    
def divicion():
    r.var = float(n1.get()) / float(n2.get())

def borrar():
    n1.set("0")
    n2.set("0")
    r.set("")

def resultado():
    r.set("0")
    if r.var >= -9:
        r.set(r.var)

# Configuración de la raíz
root = Tk()
root.title("Calculadora de 2 numeros")
root.geometry("250x240")
root.config(bd=15)

# Nombre superior
Titulo = Label(root, text="Calculadora", font="5").place(x=70, y=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

n1.set("0")
n2.set("0")

Label(root, text="Número 1" ).place(x=10, y=50)
Entry(root, justify="center", textvariable=n1).place(x=70, y=50)

Label(root, text="Número 2").place(x=10, y=80)
Entry(root, justify="center", textvariable=n2).place(x=70, y=80)

Label(root, text="Resultado").place(x=10, y=110)
Entry(root, justify="center", textvariable=r, state="disabled").place(x=70, y=110)

Label(root, text="").pack()  # Separador

Button(root, text="Sumar", command=sumar).place(x=15, y=140)
Button(root, text="Restar", command=resta).place(x=15, y=175)
Button(root, text="Mult", command=producto).place(x=70, y=140)
Button(root, text="Division", command=divicion).place(x=65, y=175)
Button(root, text="=", command=resultado).place(x=125, y=175)
Button(root, text="C", command=borrar).place(x=115, y=140)


# Finalmente bucle de la aplicación
root.mainloop()