# This is a sample Python script.
import tkinter
from cProfile import label
from tkinter import mainloop

import tk

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


root=tkinter.Tk()

root.title("Hola")

root.config(width=400, height=300, bg="#447766")
label = tkinter.Label(text="Hola", bg="yellow", fg="blue", width=10, height=5, x=20,y=20)
entry = tkinter.Entry(justify=tkinter.CENTER)
texto= tkinter.Text()
boton=tkinter.Button(text="Boton 1",x=120,y=60)
boton2=tkinter.Button(text="Boton 2",x=120,y=120)
label.pack(padx=10, pady=10)
label.place(x=100, y=100, width=40, height=20)
label.pack()
root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
mainloop()
