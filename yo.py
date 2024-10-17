import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("300x200")
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)
menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label = 'Principal', menu=menu_principal)
submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label = 'Opciones', menu=submenu)
submenu.add_command(label = 'Opción 1')
submenu.add_command(label = 'Ver Hora')
submenu.add_command(label="Salir", command=ventana.destroy)


# Crear un marco para contener la lista y la barra de desplazamiento
frame = tk.Frame(ventana)
frame.pack(fill=tk.BOTH, expand=True)

# Crear la lista de tareas
listbox = tk.Listbox(frame)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear la barra de desplazamiento
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar la lista para usar la barra de desplazamiento
listbox.config(yscrollcommand=scrollbar.set)

# Función para agregar tareas
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Crear una entrada de texto
entry = tk.Entry(ventana)
entry.pack(pady=10)

# Crear un botón para agregar tareas
add_button = tk.Button(ventana, text="Agregar Tarea", command=add_task)
add_button.pack(pady=5)

# Ejecutar el bucle principal
ventana.mainloop()