

import tkinter as tk

from tkinter import ttk



root=tk.Tk()

root.title("Actividad9_DiegoNavarroFernandez")
root.configure(width=800,height=800)


frame1 = tk.Frame(bg="red",width=400,height=400)

frame2 = tk.Frame(bg="blue",width=400,height=400)
frame3 = tk.Frame(bg="yellow",width=400,height=400)
frame4= tk.Frame(bg="green",width=400,height=400)




frame1.grid(row=0,column=0,padx= 15, pady=15)
label1=tk.Label(frame1,text="Sexo")
label1.place(x=10,y=10)
radiobutton1= ttk.Radiobutton(frame1,text="Hombre", value=1)
radiobutton1.place(x=10,y=40)
radiobutton2= ttk.Radiobutton(frame1,text="Mujer", value=1)
radiobutton2.place(x=10,y=80)


frame2.grid(row=0,column=1,padx= 15, pady=15)
label2=tk.Label(frame2,text="Nivel de estudios")
label2.place(x=10,y=10)
radiobutton3= ttk.Radiobutton(frame2,text="Estudios Basicos", value=1)
radiobutton3.place(x=10,y=40)
radiobutton4= ttk.Radiobutton(frame2,text="Estudios medios", value=1)
radiobutton4.place(x=10,y=80)
radiobutton5= ttk.Radiobutton(frame2,text="Estudios superiores", value=1)
radiobutton5.place(x=10,y=80)

frame3.grid(row=1,column=0,padx= 15, pady=15)
label3=tk.Label(frame3,text="Aficiones")
label3.place(x=10,y=10)
check1=tk.Checkbutton(frame3,text="Cine")
check1.place(x=10,y=40)
check2=tk.Checkbutton(frame3,text="Viaje")
check2.place(x=10,y=80)
check3=tk.Checkbutton(frame3,text="Deporte")
check3.place(x=10,y=120)

frame4.grid(row=1,column=1,padx= 15, pady=15)
label4=tk.Label(frame4,text="Dias disponibles")
label4.place(x=10,y=10)
check4=tk.Checkbutton(frame4,text="Lunes")
check4.place(x=10,y=40)
check5=tk.Checkbutton(frame4,text="Miercoles")
check5.place(x=10,y=80)
check6=tk.Checkbutton(frame4,text="Viernes")
check6.place(x=10,y=120)





root.mainloop()


