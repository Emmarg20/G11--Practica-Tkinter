import tkinter as tk
from tkinter import Toplevel

def tercera_ventana():
    tercera_ventana = Toplevel(ventana)
    tercera_ventana.title('Segunda ventana')
    tercera_ventana.geometry('640x480')
    boton_cerrar = tk.Button(tercera_ventana, text ='cerrar',command= tercera_ventana.destroy)
    boton_cerrar.pack(side="bottom", pady= 10)

ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label =
'Principal', menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label =
'Opciones', menu=submenu)
submenu.add_command(label = 'Reloj')
submenu.add_command(label = 'Opción 2')
submenu.add_command(label = 'Nueva ventana',command=tercera_ventana)
ventana.mainloop()