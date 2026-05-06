import tkinter as tk

from tkinter import ttk

def faryK():

    celsius = num.get()
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.8 + 32
    num2.set(fahrenheit)
    num3.set(kelvin)



root=tk.Tk()

root.title("Actividad10_DiegoNavarroFernandez")
root.configure(width=800,height=800)
txt = tk.Label(width=80,text="Temperatura en C º")

txt.place(x=50,y=40)
num=tk.DoubleVar()
entrada = tk.Entry(width=20,textvariable=num)
entrada.place(x=400,y=40)
boton=tk.Button(text="Comprobar" , command=faryK)
boton.place(x=300,y=70)
txt2 = tk.Label(width=80,text="Temperatura en F º")
txt2.place(x=50,y=120)
num2=tk.DoubleVar()
entrada2 = tk.Entry(width=20,textvariable=num2 )
entrada2.place(x=400,y=140)

txt3 = tk.Label(width=80,text="Temperatura en K º")
txt3.place(x=50,y=200)
num3=tk.DoubleVar()
entrada3 = tk.Entry(width=20,textvariable=num3)
entrada3.place(x=400,y=220)




root.mainloop()