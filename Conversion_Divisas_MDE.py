from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Conversor Monedas")

def Convertir():


        if (Divisa1.get()=="USD"):
            if(Divisa2.get()=="MXN"):
                resultado=valor.get()*19.5
                
                pass
        if (Divisa1.get()=="USD"):
            if(Divisa2.get()=="EUR"):
                resultado=valor.get()*1.45
                
                pass
        pass
        if (Divisa1.get()=="MXN"):
            if(Divisa2.get()=="USD"):
                resultado=valor.get()*0.0541
                
                pass
        pass

        if (Divisa1.get()=="MXN"):
            if(Divisa2.get()=="EUR"):
                resultado=valor.get()*(1/21)
                
                pass
        pass

        if (Divisa1.get()=="EUR"):
            if(Divisa2.get()=="USD"):
                resultado=valor.get()*(1/1.45)
                
                pass
        pass

        if (Divisa1.get()=="EUR"):
            if(Divisa2.get()=="MXN"):
                resultado=valor.get()*21
                
                pass
        pass
        return MON.set(resultado)
        pass




Principal = Frame(root, bg="GREEN")
Principal.grid()
valor=IntVar()

titulo = Label(Principal, text="Valor", font=("Roboto",10,"bold"), bg="GREEN", fg="white")
titulo.grid(row=2, column=1, padx=10, pady=10)

Numero = Entry(Principal, font=("Roboto",10), textvariable=valor).grid(row=2, column=2, padx=10, pady=10)


Divisa1=StringVar()
Divisa1.set("Moneda")
drop=OptionMenu(Principal,Divisa1,"USD","MXN","EUR")
drop.grid(row=4, column=1,padx=10, pady=10)


Divisa2=StringVar()
Divisa2.set("Moneda")
drop=OptionMenu(Principal,Divisa2,"USD","MXN","EUR")
drop.grid(row=4, column=2)

titulo = Label(Principal, text="Resultado", font=("Roboto",10,"bold"), bg="GREEN", fg="white")
titulo.grid(row=5, column=1, padx=10, pady=10)

MON=StringVar()
NUMEROB = Label(Principal, textvariable=MON, font=("Roboto",10))
NUMEROB.grid(row=5, column=2, padx=10, pady=10)


botonConvertir = Button(Principal, text="Convertir", font=("Roboto",10), command=Convertir).grid(row=6, column=1, padx=10, pady=10, columnspan=2)

root.mainloop()