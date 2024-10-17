# consultar com acceder a esta ventana desde el menu principal 
# se debe probar colores e imagenes 

import tkinter as tk
from tkinter  import Toplevel

def ventana_listas(ventana):
    ventana = Toplevel(ventana)
    ventana.title('Reloj simple')
    ventana.geometry('800x600')

    ingreso_tarea = tk.Entry(ventana)
    ingreso_tarea.pack()

    def agregar_tarea():
        tarea = ingreso_tarea.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)
            ingreso_tarea.delete(0, tk.END)

    boton_agregar = tk.Button(ventana, text = 'Agregar tarea', command = agregar_tarea)
    boton_agregar.pack()

    def eliminar_tarea():
        seleccion = lista_tareas.curselection()
        if seleccion:
            lista_tareas.delete(seleccion)

    boton_eliminar = tk.Button(ventana, text = 'Eliminar tarea', command = eliminar_tarea)
    boton_eliminar.pack()
    lista_tareas = tk.Listbox(ventana)
    lista_tareas.pack() 