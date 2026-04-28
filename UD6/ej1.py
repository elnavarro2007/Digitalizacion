import tkinter as tk

from tkinter import ttk

texto = tk.StringVar()

Etiqueta = tk.Label(textvariable=texto)
texto.set("Hola")


mainloop()