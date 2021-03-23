from tkinter import *
from tkinter import messagebox

global solucion, cartas

cartas = []
solucion = []

#Ventana Pricipal------------------------------------------------------------------------

def ven_prin(): # ventana principal
    #Ventana principal

    ven = Tk()
    ven.title("Crime Investigation - El Juego")
    ven.iconbitmap('lupa.ico')
    ven.geometry('800x450+350+150')
    ven.resizable(width= False, height= False)

    titu = Label(ven, text= "Crime Investigation - El Juego", bg= "sienna3", fg= "white", font=("Times", 18), padx= 40)
    titu.place(x= 202, y= 20)

    #Cartas de la solucion
    solu_tex = Label(ven, text= "Cartas de la Solición", fg= "sienna3", font=("Times", 16))
    solu_tex.place(x= 300, y= 60)


    
    
    ven.mainloop()

ven_prin()