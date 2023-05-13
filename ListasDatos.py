#Flores Romero Andres Gael
#13/05/2023

#Importacion para Tkinter
from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox

#---------------FUNCIONES-------------------------

def BorrarContenido():
    nombreVar.set("")
    APaternoVar.set("")
    AMaternoVar.set("")
    CorreoVar.set("")
    NumeroMovilVar.set("")
    Estados.set("")
    Leer.set(False)
    Musica.set(False)
    VideoJuegos.set(False)
    Obligacion.set(None)


def guardar_datos():

    with open("Listas.csv", "r") as file:
        file.readlines
    
    Nombre = nombreVar.get()
    APaterno = APaternoVar.get()
    AMaterno = AMaternoVar.get()
    Correo = CorreoVar.get()
    Numero = NumeroMovilVar.get()
    SelecEstados = Estados.get()
    LeerOp = "Si" if Leer.get() == True else "No"
    MusicaOp = "Si" if Musica.get() == True else "No"
    VideoJuegosOp = "Si" if VideoJuegos.get() == True else "No"
    Obli = Obligacion.get()

    if not Nombre or not APaterno or not AMaterno or not Correo or not Numero or not LeerOp or not MusicaOp or not VideoJuegosOp or not Obli or not SelecEstados:
        messagebox.showinfo("ERROR", "Las casillas deben estar llenas para guardar.")
    else:
        with open("Listas.csv","a") as file:
            file.write(f'{Nombre},{APaterno},{AMaterno},{Correo},{Numero},{LeerOp},{MusicaOp},{VideoJuegosOp},{Obli},{SelecEstados}\n') 
        BorrarContenido()
    
    tv.insert(parent="", index="end", iid=random.randint(1,1000), text=random.randint(1,1000), values=(Nombre, APaterno, AMaterno, Correo, Numero, LeerOp, MusicaOp, VideoJuegosOp,SelecEstados))

#---------------------------------PADRE--------------------------------------

root = Tk()
root.title("Listas en CSV")

#---------------------------------FRAMES--------------------------------------

#Principal
mainFrame = ttk.Frame(root)
mainFrame.grid(column=0, row=0)

#Inicial
FrameInicial = ttk.Frame(mainFrame)
FrameInicial.grid(column=0,row=0)

#Lado izquierdo Inicial
Izquierda = ttk.Frame(FrameInicial, relief="raised", width= 20, height= 20)
Izquierda.grid(column=0, row=0, sticky=(W), padx=10, pady=10)

#Lado Derecho Inicial
Derecha = ttk.Frame(FrameInicial, relief="raised", width= 20, height= 20)
Derecha.grid(column=1, row=0, sticky=(W), padx=10, pady=10)

#Frames Izquierda
FrameDatos1 = ttk.Frame(Izquierda, relief="raised", width= 20, height= 20)
FrameDatos1.grid(column=0, row=0, sticky=(W), padx=10, pady=10)

FrameDatos2= ttk.Frame(Izquierda, relief="raised", width= 20, height= 20)
FrameDatos2.grid(column=0, row=1, padx=10, pady=10)

FrameDatos3= ttk.Frame(Izquierda, relief="raised", width= 20, height= 20)
FrameDatos3.grid(column=0, row=2, padx=10, pady=10)

#Frames Derecha
FrameDatos4 = ttk.Frame(Derecha, relief="raised", width= 20, height= 20)
FrameDatos4.grid(column=0, row=0, sticky=(N,W), padx=10, pady=10)

FrameDatos5= ttk.Frame(Derecha,  relief="raised", width= 20, height= 20)
FrameDatos5.grid(column=0, row=1, padx=10, pady=10)


#-----------------------------------Variables-------------------------------------

#Variables Var
nombreVar = StringVar()
APaternoVar = StringVar()
AMaternoVar = StringVar()
CorreoVar = StringVar()
NumeroMovilVar = StringVar()
Leer = BooleanVar()
Musica = BooleanVar()
VideoJuegos = BooleanVar()
Obligacion = StringVar(value=0)
Estados = StringVar()

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

CheckLeer = ttk.Checkbutton(FrameDatos2, text="Leer", variable=Leer,width="10").grid(column=0,row=0,pady=5, sticky=(W))
CheckMusica = ttk.Checkbutton(FrameDatos2, text="Musica", variable=Musica, width="10").grid(column=1,row=0,pady=5, padx=5, sticky=(W))
CheckVJ = ttk.Checkbutton(FrameDatos2, text="Videojuegos", variable=VideoJuegos, width="10").grid(column=2,row=0,pady=5, padx=5, sticky=(W))

#----------------------------------Frame Izquierda 3-------------------------------------

ttk.Button(FrameDatos3, text="Guardar", command=guardar_datos).grid(column=0, row=0, sticky=(E))
ttk.Button(FrameDatos3, text="Borrar", command=BorrarContenido).grid(column=1, row=0,sticky=(E))

#----------------------------------Frame Derecha 1-------------------------------------

RadioEst = ttk.Radiobutton(FrameDatos4, text="Estudiante", variable=Obligacion, value="Estudiante", width="10").grid(column=0, row=0, sticky=(N)) 
RadioEmp = ttk.Radiobutton(FrameDatos4, text="Empleado", variable=Obligacion, value="Empleado", width="10").grid(column=0 , row=1, sticky=(N)) 
RadioDesemp = ttk.Radiobutton(FrameDatos4, text="Desempleado", variable=Obligacion, value="Desempleado", width="10").grid(column=0, row=2, sticky=(N)) 

#----------------------------------Frame Derecha 2-------------------------------------

ttk.Label(FrameDatos5, text= "Estados: ",  width="15",anchor="w").grid(column=0, row=0, sticky=(E))
comboEstados = ttk.Combobox(FrameDatos5, textvariable=Estados, state="readonly")
comboEstados.grid(column=1, row=0)
comboEstados['values'] = ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila", 
                        "Colima", "Chiapas", "Chihuahua", "Ciudad de Mexico", "Durango", "Guanajuato", 
                        "Guerrero", "Hidalgo", "Jalisco", "Mexico", "Michoacan", "Morelos", "Nayarit", 
                        "Nuevo Leon", "Oaxaca", "Puebla", "Queretaro", "Quintana Roo", "San Luis Potosi", 
                        "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatan", "Zacatecas")


#----------------------------------Ventana Tabla------------------------------------------
Tabla = Tk()
Tabla.title("Tabla Lista de Datos (CSV)")

FrameTabla = ttk.Frame(Tabla)
FrameTabla.grid(column=0, row=0)

tv = ttk.Treeview(FrameTabla, columns=("nombreVar","APaternoVar", "AMaternoVar", "CorreoVar", "NumeroMovilVar", "Leer", "Musica", "VideoJuegos", "Obligacion", "Estados"))
tv.grid(column=0, row=0, padx=0, pady=0)
tv.column("#0",width=20)
tv.column("nombreVar",width=130, anchor=CENTER)
tv.column("APaternoVar",width=130, anchor=CENTER)
tv.column("AMaternoVar",width=130, anchor=CENTER)
tv.column("CorreoVar",width=130, anchor=CENTER)
tv.column("NumeroMovilVar",width=130, anchor=CENTER)
tv.column("Leer",width=130, anchor=CENTER)
tv.column("Musica",width=130, anchor=CENTER)
tv.column("VideoJuegos",width=130, anchor=CENTER)
tv.column("Obligacion",width=130, anchor=CENTER)
tv.column("Estados",width=130, anchor=CENTER)

tv.heading("#0", text="ID", anchor=CENTER)
tv.heading("nombreVar", text="Nombre", anchor=CENTER)
tv.heading("APaternoVar", text="APaterno", anchor=CENTER)
tv.heading("AMaternoVar", text="AMaterno", anchor=CENTER)
tv.heading("CorreoVar", text="Correo", anchor=CENTER)
tv.heading("NumeroMovilVar", text="Movil", anchor=CENTER)
tv.heading("Leer", text="Leer", anchor=CENTER)
tv.heading("Musica", text="Musica", anchor=CENTER)
tv.heading("VideoJuegos", text="VideoJuegos", anchor=CENTER)
tv.heading("Obligacion", text="Obligacion", anchor=CENTER)
tv.heading("Estados", text="Estado", anchor=CENTER)

root.mainloop()


