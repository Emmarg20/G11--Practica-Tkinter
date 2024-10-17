import tkinter as tk
from tkinter import Toplevel

def tercera_ventana(ventana):
    tercera_ventana = Toplevel(ventana)
    tercera_ventana.title('Tercer Ventana')
    tercera_ventana.geometry('640x480')
    boton_cerrar = tk.Button(tercera_ventana, text ='cerrar',command= tercera_ventana.destroy)
    boton_cerrar.pack(side="bottom", pady= 10)