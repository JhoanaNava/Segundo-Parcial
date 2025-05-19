import tkinter as tk
from tkinter import messagebox

def mostrar_saludo():
    nombre = entrada_nombre.get()

    if nombre.strip() == "":
        messagebox.showwarning("Advertencia", "Por favor ingresa tu nombre")
        return

    ventana_inicio.destroy()  # Cierra la primera ventana

    # Crear la segunda ventana
    ventana_saludo = tk.Tk()
    ventana_saludo.title("Saludo")

    mensaje = f"Hola, {nombre}!"
    tk.Label(ventana_saludo, text=mensaje, font=("Arial", 16)).pack(pady=20)
    tk.Button(ventana_saludo, text="Cerrar", command=ventana_saludo.destroy).pack(pady=10)

    ventana_saludo.mainloop()

# Crear la primera ventana
ventana_inicio = tk.Tk()
ventana_inicio.title("Ingresa tu nombre")

tk.Label(ventana_inicio, text="¿Cuál es tu nombre?").grid(row=0, column=0, padx=10, pady=10)
entrada_nombre = tk.Entry(ventana_inicio)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Button(ventana_inicio, text="Aceptar", command=mostrar_saludo, bg="blue", fg="white").grid(row=1, column=0, columnspan=2, pady=10)

ventana_inicio.mainloop()
