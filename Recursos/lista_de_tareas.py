import tkinter as tk

ventana = tk.Tk()
ventana.title('Lista de tareas')
ventana.geometry('400x200')

ingreso_tarea = tk.Entry(ventana)
ingreso_tarea.pack()

def agregar_tarea():
tarea = ingreso_tarea.get()
if tarea:
lista_tareas.insert(tk.END, tarea)
ingreso_tarea.delete(0, tk.END)

boton_agregar = tk.Button(ventana, text = 'Agregar
tarea', command = agregar_tarea)
boton_agregar.pack()

def eliminar_tarea():
seleccion = lista_tareas.curselection()
if seleccion:
lista_tareas.delete(seleccion)

boton_eliminar = tk.Button(ventana, text = 'Eliminar
tarea', command = eliminar_tarea)
boton_eliminar.pack()

‌

lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()

ventana.mainloop()