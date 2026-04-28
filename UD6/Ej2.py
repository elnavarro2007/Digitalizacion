import tkinter as tk
import random


from tkinter import ttk, StringVar


def ganado ():
    num = num2.get()
    if num == n1:
       resultado = tk.Label(text="Has ganado")
       resultado.place(x=150,y=150)
    else:
        resultado = tk.Label(text="Has perdido")
        resultado.place(x=150,y=150)





root=tk.Tk()

root.title("Actividad2_DiegoNavarroFernandez")
root.configure(width=640,height=480)




txt = tk.Label(width=80,text="Adivina el numero del 1 al 10")
txt.place(x=10,y=10)



n1 = random.randint(1,10)
print(n1)



boton=tk.Button(text="comprobar", command=ganado)
boton.place(x=200,y=200)
num2=tk.IntVar()

entrada = tk.Entry(width=80,textvariable=num2)


entrada.place(x=10,y=100)

root.mainloop()