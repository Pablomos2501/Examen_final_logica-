"""
logica en sistemas
primer semestre 
Pablo Otoniel Moscoso Flores
0907-19-2477
"""
from tkinter import *
#funcion del primer boton 
def calcular():
    if v1.get() < v3.get():
        messagebox.showinfo("multiplicar",f" se esta multiplicando   y la respuesta es   {v1.get() * v2.get() * v3.get() }   ")
    elif v1.get() == v3.get():
        messagebox.showinfo("sumar",f" se esta sumando   y la respuesta es   {v1.get() + v2.get() + v3.get() }   ")
    if v2.get() == 0 and v1.get() < v3.get():
        messagebox.showinfo("restando",f" se esta restando   y la respuesta es   {v1.get() - v3.get() }  ")
    if v2.get() == 0 and v3.get() < v1.get():
        messagebox.showinfo("restando",f" se esta restando   y la respuesta es   {v3.get() - v1.get() }   ")
#funcion del segundo boton 
def concatenar():
    for x in 0:
        if v1.get()  v2.get():
            messagebox.showinfo("multiplicar",f" se esta multiplicando   y la respuesta es   {v1.get() * v2.get() + v3.get() }   ")

#interfaz
interfaz=Tk()
interfaz.geometry("500x300+100+100")
interfaz.title("examen")

#labeles y entradas 
lbl=Label(text="valor 1").place(x=10,y=40)
v1=IntVar()
ingreso=Entry(interfaz,textvariable=v1).place(x=60,y=40)

lbl2=Label(text="valor 2").place(x=10,y=90)
v2=IntVar()
ingreso=Entry(interfaz,textvariable=v2).place(x=60,y=90)

lbl3=Label(text="valor 3").place(x=10,y=120)
v3=IntVar()
ingreso=Entry(interfaz,textvariable=v3).place(x=60,y=120)
#botones
boton=Button(interfaz,text="calcular",command=calcular).place(x=10,y=150)
boton2=Button(interfaz,text="concatenar", command=concatenar).place(x=10,y=180)


interfaz.mainloop()