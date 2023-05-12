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

#Principal
mainFrame = ttk.Frame(root, background="cyan4")
mainFrame.grid(column=0, row=0)

#Inicial
FrameInicial = ttk.Frame(mainFrame, background="cyan4")
FrameInicial.grid(column=0,row=0)

#Lado izquierdo Inicial
Izquierda = ttk.Frame(FrameInicial, relief="raised", width= 20, height= 20, background="cyan4")
Izquierda.grid(column=0, row=0, sticky=(W), padx=10, pady=10)

#Lado Derecho Inicial
Derecha = ttk.Frame(FrameInicial, relief="raised", width= 20, height= 20, background="cyan4")
Derecha.grid(column=1, row=0, sticky=(W), padx=10, pady=10)

#Frames Izquierda
FrameDatos1 = ttk.Frame(Izquierda, relief="raised", width= 20, height= 20, background="cyan4")
FrameDatos1.grid(column=0, row=0, sticky=(W), padx=10, pady=10)

FrameDatos2= ttk.Frame(Izquierda, background="cyan4")
FrameDatos2.grid(column=0, row=1)

FrameDatos3= ttk.Frame(Izquierda, background="cyan4")
FrameDatos3.grid(column=0, row=2)

#Frames Derecha
FrameDatos4 = ttk.Frame(Derecha, relief="raised", width= 20, height= 20, background="cyan4")
FrameDatos4.grid(column=0, row=0, sticky=(W), padx=10, pady=10)

FrameDatos5= ttk.Frame(Derecha, background="cyan4")
FrameDatos5.grid(column=0, row=1)


#-----------------------------------Variables-------------------------------------

#Variables Var
nombreVar = StringVar()
APaternoVar = StringVar()
AMaternoVar = StringVar()
CorreoVar = StringVar()
NumeroMovilVar = StringVar()
Estados = StringVar()
Gustos1 = IntVar()
Gustos2 = IntVar()
Gustos3 = IntVar()
Obligacion = IntVar(value=0)

#----------------------------------Frame Izquierda 1-------------------------------------

#Entrys
NombreEntry = ttk.Entry(FrameDatos1, textvariable=nombreVar, width=26, ).grid(column=1, row=0,pady=5)
APaternoEntry = ttk.Entry(FrameDatos1, textvariable=APaternoVar, width=26).grid(column=1, row=1,pady=5)
AMaternoEntry = ttk.Entry(FrameDatos1, textvariable=AMaternoVar, width=26).grid(column=1, row=2,pady=5)
CorreoEntry = ttk.Entry(FrameDatos1, textvariable=CorreoVar, width=26).grid(column=1, row=3,pady=5)
NumeroEntry = ttk.Entry(FrameDatos1, textvariable=NumeroMovilVar, width=26).grid(column=1, row=4,pady=5)

#Labels
ttk.Label(FrameDatos1, text= "Nombre: ", width="15", anchor="w").grid(column=0, row=0, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "A. Paterno: ",  width="15", anchor="w").grid(column=0, row=1, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "A. Materno: ",  width="15", anchor="w").grid(column=0, row=2, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "Correo: ",  width="15", anchor="w").grid(column=0, row=3, pady= 5, sticky=(E))
ttk.Label(FrameDatos1, text= "Movil: ",  width="15",anchor="w").grid(column=0, row=4, pady= 5, sticky=(E))

#----------------------------------Frame Izquierda 2-------------------------------------
#Tercer Frame

CheckLeer = ttk.Checkbutton(FrameDatos2, text="Leer", variable=Gustos1).grid(column=0,row=1,pady=5, sticky=(W))
CheckMusica = ttk.Checkbutton(FrameDatos2, text="Musica", variable=Gustos2).grid(column=1,row=1,pady=5, padx=5, sticky=(W))
CheckVJ = ttk.Checkbutton(FrameDatos2, text="Videojuegos", variable=Gustos3).grid(column=2,row=1,pady=5, padx=5, sticky=(W))

#----------------------------------Frame Izquierda 3-------------------------------------

ttk.Button(FrameDatos3, text="Guardar", command=guardar_datos).grid(column=0, row=0, sticky=(E), pady=10)
ttk.Button(FrameDatos3, text="Borrar", command=BorrarContenido).grid(column=1, row=0,sticky=(E), pady=10, padx=25)

#----------------------------------Frame Derecha 1-------------------------------------

RadioEst = ttk.Radiobutton(FrameDatos4, text="Estudiante", variable=Obligacion, value=1, background="cyan2").grid(column=0, row=0, sticky=(W)) 
RadioEmp = ttk.Radiobutton(FrameDatos4, text="Empleado", variable=Obligacion, value=2, background="cyan2").grid(column=0 , row=1, sticky=(W)) 
RadioDesemp = ttk.Radiobutton(FrameDatos4, text="Desempleado", variable=Obligacion, value=3, background="cyan2").grid(column=0, row=2, sticky=(W)) 

#----------------------------------Frame Derecha 2-------------------------------------




root.mainloop()


