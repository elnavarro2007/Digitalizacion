import tkinter as tk
from tkinter import ttk





class Boton:
 def __init__(self,texto,fila,columna):
    self.boton = tk.Button(
        text= texto,
         bg= "black",
         fg= "green",
         font=("Arial",20,"bold"),
         width=3,
         height=2

    )


    self.boton.grid(row=fila,column=columna,padx=5,pady=5)
root=tk.Tk()

root.title("Actividad10_DiegoNavarroFernandez")
root.configure(width=800,height=800)
BotonResultado = tk.Button(text="Resultado", bg= "black",fg="green", width=40 )
resultado = tk.StringVar()
BotonResultado.grid(row=0,columnspan=4,padx=5,pady=5)
Boton1 = Boton("7",1,0)
Boton2 = Boton("8",1,1)
Boton3 = Boton("9",1,2)
BotonDiv = Boton("/",1,3)
BotonMulti = Boton("*",2,3)
BotonResto = Boton("-",3,3)
BotonSuma = Boton("+",4,3)
BotonReset = Boton("Reset",4,1)
BotonDecimal = Boton(".",4,2)



Boton4 = Boton("6",2,0)
Boton5 = Boton("5",2,1)
Boton6 = Boton("4",2,2)
Boton7 = Boton("3",3,0)
Boton8 = Boton("2",3,1)
Boton9 = Boton("1",3,2)
Boton10 = Boton("0",4,0)





root.mainloop()