import tkinter as tk
from tkinter import ttk

# Función para agregar información a la lista
def agregar_info():
    info = campo_texto.get()
    if info:
        lista_datos.insert(tk.END, info)
        campo_texto.delete(0, tk.END)

# Función para limpiar la lista y el campo de texto
def limpiar_lista():
    lista_datos.delete(0, tk.END)
    campo_texto.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de GUI")

# Crear y colocar etiquetas (labels)
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=5)

# Crear y colocar campo de texto
campo_texto = tk.Entry(ventana, width=50)
campo_texto.pack(pady=5)

# Crear y colocar botones
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Crear y colocar una lista (listbox) para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
