from tkinter import *
canvas = Canvas(width=1280, height=720, bg="white")
canvas.pack(expand=YES, fill=BOTH)
x = 100
y = 300
for i in range(10):

    canvas.create_oval(x,x,y,y,fill="red", width=10, outline="red")
    x = x+5
    y = y-5
    canvas.create_oval(x, x, y, y, fill="white", width=10, outline="white")
    x = x+5
    y = y-5







mainloop()