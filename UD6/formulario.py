import tkinter as tk
from tkinter import ttk


class Etiqueta:
    def __init__(self, texto, fila):
        self.label = tk.Label(text=texto, font=("Arial", 11), fg="blue")
        self.label.grid(row=fila, column=0, padx=10, pady=5)

# para poner comentarios con el arroba
# pasarle los parametros necesarios a la clase y despues que al crear la variable esta pueda
# pillarlos al usar la clase
class Texto:
    def __init__(self, fila,w):
        self.label = tk.Entry(width=w, font=("Arial", 11), fg="black")
        self.label.grid(row=fila, column=1, padx=10, pady=5,sticky="w")


root=tk.Tk()
root.title("Formulario ejercicio 2 digitalizacion")
root.geometry("500x500")
nombreEtiqueta = Etiqueta("Nombre",0)
nombre = Texto(0,20)

apellidosEtiqueta = Etiqueta("Apellidos",1)
apellidos = Texto(1,10)

direccionEtiqueta = Etiqueta("Direccion",2)
direccion = Texto(2,40)
cpEtiqueta = Etiqueta("CP",3)
cp = Texto(3,50)
localidadEtiqueta = Etiqueta("Localidad",4)
localidad = Texto(4,10)
provinciaEtiqueta = Etiqueta("Provincia",5)
provincia = Texto(5,12)
paisEtiqueta = Etiqueta("Pais",6)
pais = Texto(6,25)
edadEtiqueta = Etiqueta("Edad",7)
edad = Texto(7,23)
profesionEtiqueta = Etiqueta("Profesion",8)
profesion = Texto(8,15)


root.mainloop()