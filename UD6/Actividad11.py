import tkinter as tk
from tkinter import ttk


class Etiqueta:
    def __init__(self, texto, fila,color):
        self.label = tk.Label(text=texto, font=("Arial", 11), fg=color)
        self.label.grid(row=fila, column=1, padx=10, pady=5)



# para poner comentarios con el arroba
# pasarle los parametros necesarios a la clase y despues que al crear la variable esta pueda
# pillarlos al usar la clase


class Boton:
 def __init__(self,texto,fila):
    self.boton = tk.Button(
        text= texto,
         bg= "blue",
         fg= "white",
         font=("Arial",12,"bold"),


    )


    self.boton.grid(row=fila,column=2,padx=5,pady=5)

class verificarCheck :
    def __init__(self, checkbutton, texto,fila,color):
        self.checkbutton = tk.Checkbutton(text=texto, variable=checkbutton,fg=color)

        self.checkbutton.grid(row=fila, column=0, padx=5, pady=5, sticky="w")


root=tk.Tk()
root.title("Actividad 11 Diego Navarro Fernandez")
root.geometry("500x500")
lunes = verificarCheck("Lunes","Lunes",0,"green")
borrar = Boton("Borrar todo",0)

martes = verificarCheck("martes","Martes",1,"green")
seleccionar = Boton("Seleccionar todo",1)

miercoles = verificarCheck("miercoles","miercoles",2,"green")
anterior = Boton("Anterior",2)

jueves = verificarCheck("Jueves","jueves",3,"green")
siguiente = Boton("Siguiente",3)

viernes = verificarCheck("viernes","viernes",4,"green")
guardar = Boton("Guardar",4)

sabado = verificarCheck("sabado","sabado",5,"red")

domingo = verificarCheck("domingo","domingo",6,"red")
salir = Boton("salir",6)

root.mainloop()