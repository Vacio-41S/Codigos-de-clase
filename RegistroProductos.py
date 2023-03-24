from tkinter import*
from PIL import ImageTk,Image
root= Tk()

ventanaPrincipal=Frame(root,bg="green")
ventanaPrincipal.grid()
valor=StringVar()

imgPROD=Image.open("prod.png") 
imagenmusica=imgPROD.resize((70,70))
imag=ImageTk.PhotoImage(imagenmusica)
miTitulo=Label(ventanaPrincipal,image=imag)
miTitulo.grid(row=2,column=0,padx=10,pady=20,columnspan=2,rowspan=2)
titulo=Label(ventanaPrincipal,text="Registro de Productos",font=("Roboto",20),bg="green").grid(row=1,column=0,columnspan=2)


textoNombre=Entry(ventanaPrincipal,font=("Roboto",15)).grid(row=4,column=1,padx=10,pady=10)
textoNombre=Entry(ventanaPrincipal,font=("Roboto",15)).grid(row=5,column=1,padx=10,pady=20)
opciones=['INTEL','AMD','MARCA CHINA']
opcion=OptionMenu(ventanaPrincipal,valor,*opciones).grid(row=8,column=1,padx=40,pady=40)

titulo=Label(ventanaPrincipal,text="Producto:",font=("Roboto",15),bg="green").grid(row=4,column=0)
titulo=Label(ventanaPrincipal,text="Sku:",font=("Roboto",15),bg="green").grid(row=5,column=0)
titulo=Label(ventanaPrincipal,text="Depto:",font=("Roboto",15),bg="green").grid(row=6,column=0)
titulo=Label(ventanaPrincipal,text="Proveedor:",font=("Roboto",15),bg="green").grid(row=8,column=0,padx=20,pady=10)
titulo=Label(ventanaPrincipal,text="Idioma:",font=("Roboto",15),bg="green").grid(row=9,column=0)

control=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="A",variable=control,font=("Roboto",10),bg="green")
preserve.grid(row=7,column=0,pady=20,padx=10)
contro2=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="B",variable=contro2,font=("Roboto",10),bg="green")
preserve.grid(row=7,column=1,pady=20,padx=10)
contro3=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="C",variable=contro3,font=("Roboto",10),bg="green")
preserve.grid(row=7,column=2,pady=20,padx=10)
contro4=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="EN",variable=contro4,font=("Roboto",10),bg="green")
preserve.grid(row=10,column=0,pady=20)
contro5=IntVar()
preserve=Checkbutton(ventanaPrincipal,text="SP",variable=contro5,font=("Roboto",10),bg="green")
preserve.grid(row=10,column=1,pady=20)

botonCerrar=Button(ventanaPrincipal,text="REGISTRAR",command=root.destroy,width=20,height=2).grid(row=11 , column=0,padx=10,pady=10,columnspan=2)

root.mainloop()