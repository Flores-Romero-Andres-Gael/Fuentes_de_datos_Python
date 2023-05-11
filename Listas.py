#Flores Romero Andres Gael
#27/04/2023

#Importacion para Tkinter
from tkinter import *
from tkinter import ttk
import tkinter as ttk
from tkinter import messagebox

#---------------FUNCIONES-------------------------

def BorrarContenido():
    nombreVar.set("")
    APaternoVar.set("")
    AMaternoVar.set("")
    CorreoVar.set("")
    NumeroMovilVar.set("")

def guardar_datos():

    with open("Listas.csv", "r") as file:
        print(file.readlines)
    
    Nombre = nombreVar.get()
    APaterno = APaternoVar.get()
    AMaterno = AMaternoVar.get()
    Correo = CorreoVar.get()
    Numero = NumeroMovilVar.get()

    if not Nombre or not APaterno or not AMaterno or not Correo or not Numero:
            messagebox.showinfo("ERROR", "Las casillas deben estar llenas para guardar.")
    else:
        with open("Listas.csv","a") as file:
            file.write(f'{Nombre},{APaterno},{AMaterno},{Correo},{Numero}\n') 
        BorrarContenido()

#---------------------------------PADRE--------------------------------------
root = Tk()
root.title("Listas en CSV")

#---------------------------------FRAMES--------------------------------------

#Primero
mainFrame = ttk.Frame(root, background="cyan4")
mainFrame.grid(column=0, row=0)

FrameDatos = ttk.Frame(mainFrame, background="cyan4")
FrameDatos.grid(column=0,row=0)

#Segundo
mainFrame2 = ttk.Frame(FrameDatos, relief="raised", width= 20, height= 20, background="cyan4")
mainFrame2.grid(column=0, row=0, sticky=(W), padx=10, pady=10)


#-----------------------------------DATOS-------------------------------------
#PrimerFrame

#SegundoFrame
nombreVar = StringVar()
APaternoVar = StringVar()
AMaternoVar = StringVar()
CorreoVar = StringVar()
NumeroMovilVar = StringVar()

#----------------------------------ENTRYS-------------------------------------
#SegundoFrame

NombreEntry = ttk.Entry(mainFrame2, textvariable=nombreVar, width=26).grid(column=1, row=0,pady=5)
APaternoEntry = ttk.Entry(mainFrame2, textvariable=APaternoVar, width=26).grid(column=1, row=1,pady=5)
AMaternoEntry = ttk.Entry(mainFrame2, textvariable=AMaternoVar, width=26).grid(column=1, row=2,pady=5)
CorreoEntry = ttk.Entry(mainFrame2, textvariable=CorreoVar, width=26).grid(column=1, row=3,pady=5)
NumeroEntry = ttk.Entry(mainFrame2, textvariable=NumeroMovilVar, width=26).grid(column=1, row=4,pady=5)

#----------------------------------LABELS------------------------------------

#Segundo Frame
ttk.Label(mainFrame2, text= "Nombre: ", width="15", anchor="w").grid(column=0, row=0, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "A. Paterno: ",  width="15", anchor="w").grid(column=0, row=1, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "A. Materno: ",  width="15", anchor="w").grid(column=0, row=2, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "Correo: ",  width="15", anchor="w").grid(column=0, row=3, pady= 5, sticky=(E))
ttk.Label(mainFrame2, text= "Movil: ",  width="15",anchor="w").grid(column=0, row=4, pady= 5, sticky=(E))

#----------------------------------BOTTONS-------------------------------------
#Primer Frame
FrameGC = ttk.Frame(FrameDatos, background="cyan4")
FrameGC.grid(column=0, row=1)

ttk.Button(FrameGC, text="Guardar", command=guardar_datos).grid(column=0, row=0, sticky=(E), pady=10)
ttk.Button(FrameGC, text="Borrar", command=BorrarContenido).grid(column=1, row=0,sticky=(E), pady=10, padx=25)



root.mainloop()


