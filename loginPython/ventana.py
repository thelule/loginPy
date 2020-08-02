from tkinter import *

""" class interfaz:
    def __init__(self, contenedor):
        self.e1 = Label(contenedor, text = "Etiqueta1", fg = "black", bg = "white")
        self.e2 = Label(contenedor, text = "Etiqueta2", fg = "black", bg = "green")
        self.e3 = Label(contenedor, text = "Etiqueta3", fg = "black", bg = "blue")
        self.e1.pack(side = TOP)
        self.e3.pack(side = BOTTOM, fill = X)
        self.e2.pack(side = RIGHT) """

""" 
class interfaz:
    def __init__(self, contenedor):
        self.e1 = Label(contenedor, text = "Etiqueta1", fg = "black", bg = "white")
        self.e2 = Label(contenedor, text = "Etiqueta2", fg = "black", bg = "green")
        self.e3 = Label(contenedor, text = "Etiqueta3", fg = "black", bg = "blue")
        self.e4 = Label(contenedor, text = "Etiqueta4", fg = "black", bg = "orange")
        self.e5 = Label(contenedor, text = "Etiqueta5", fg = "black", bg = "red")
        self.e6 = Label(contenedor, text = "Etiqueta6", fg = "black", bg = "violet")
        self.e1.grid(column=0, row=0)
        self.e2.grid(column=0, row=1)
        self.e3.grid(column=0, row=2)
        self.e4.grid(column=1, row=0)
        self.e5.grid(column=1, row=1)
        self.e6.grid(column=1, row=2) """

""" class interfaz:
    def __init__(self, contenedor):
        self.e1 = Label(contenedor, text = "Etiqueta1", fg = "black", bg = "white")
        self.e1.place(x=10, y=10, width=100, height=100) """


class interfaz:
    def __init__(self, contenedor):
        self.textoE3 = StringVar()
        self.e1 = Label(contenedor, text = "Convertir celcius a farenheight", fg = "black")
        self.e2 = Label(contenedor, text = "Celcius", fg = "black")
        self.e3 = Label(contenedor, text = "Farenheight", fg = "black")
        self.e4 = Button(contenedor, text = "Convertir", fg = "black", bg = "orange", command=self.hacerConversion)
        self.e5 = Entry(contenedor, fg = "black", bg = "red")
        self.e6 = Label(contenedor, text = "", fg = "black", textvariable=self.textoE3)
        self.e1.grid(column=0, row=0, columnspan=2)
        self.e2.grid(column=0, row=1)
        self.e3.grid(column=0, row=2)
        self.e4.grid(column=1, row=3, columnspan=2)
        self.e5.grid(column=1, row=1)
        self.e6.grid(column=1, row=2)
    
    def hacerConversion(self):
        cel = float(self.e5.get())
        far = (cel*1.8)+32
        self.textoE3.set(far)
        

ventana = Tk()
interfaz1 = interfaz(ventana)
ventana.mainloop()