# consultar com acceder a esta ventana desde el menu principal 
# como acceder al reloj desde el menu principal reloj
# se debe probar colores e imagenes par dar estilos

import tkinter as tk
from tkinter import Toplevel # crea nuevas ventanas en niveles.
from seccion_3 import * # imprta elementos y funciones de el archivo ventana_3.py"
from reloj import *
from lista_tareas import *

#crea una segunda ventana nueva 
def segunda_ventana():
    segunda_ventana = Toplevel(ventana)
    segunda_ventana.title('Segunda ventana')
    segunda_ventana.geometry('640x480')
    boton_cerrar = tk.Button(segunda_ventana, text ='cerrar',command= segunda_ventana.destroy)
    boton_cerrar.pack(side="bottom", pady= 10)

# venatana principal.
ventana = tk.Tk()
ventana.title('Grupo 11')
ventana.geometry('400x200')
#ventana.iconbitmap("11.ico") 


barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu)

menu_horario = tk.Menu(barra_menu)
barra_menu.add_cascade(label = 'Informatorio', menu=menu_principal)
#Reloj
submenub = tk.Menu(menu_horario)
barra_menu.add_cascade(label = 'Reloj', menu = menu_horario)
menu_horario.add_cascade(label = 'Consultar hora', menu=submenub,) #colocar para ira la ventana reloj


#Reloj
#sub menu principal
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label = 'Modulos', menu=submenu)
menu_principal.add_command(label="Salir", command=ventana.destroy)
submenu.add_command(label = 'Segunda ventana',command=segunda_ventana)
# comando que lleva hacia
submenu.add_command(label = 'Tercera ventana',command= lambda:tercera_ventana (ventana))
submenu.add_command(label = 'Hora',command= lambda: Ventana_hora(ventana))
submenu.add_command(label = 'Listas',command= lambda: ventana_listas(ventana))

ventana.mainloop()