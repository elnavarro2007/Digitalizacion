import tkinter as tk

from tkinter import ttk

def uno ():
    nun.set(1)
def dos ():
    nun.set(2)



root=tk.Tk()

root.title("Actividad3_DiegoNavarroFernandez")
root.configure(width=800,height=800)
boton=tk.Button(text="uno" , command=uno)
boton.place(x=10,y=10)
boton2=tk.Button(text="dos", command=dos)
boton2.place(x=80,y=10)
nun=tk.StringVar()

texto = tk.Entry(width=35, textvariable=nun)
texto.place(x=10,y=80)

root.mainloop()