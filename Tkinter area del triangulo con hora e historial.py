import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Área del Círculo PRO")
ventana.geometry("400x500")
ventana.configure(bg="lightblue") 

# Variables
contador = 0
historial = []

# Función para calcular el área
def calcular_area():
    global contador, historial
    try:
        radio = float(entrada.get())
        area = math.pi * radio ** 2
        contador += 1

        resultado.config(text=f"El área es: {area:.2f}")

        if area > 100:
            mensaje.config(text="Área GRANDE", fg="red") 
        else:
            mensaje.config(text="Área PEQUEÑA", fg="green")  

        hora = datetime.now().strftime("%H:%M:%S")
        historial.append((radio, area, hora))
        actualizar_historial()

        total_label.config(text=f"Total de cálculos: {contador}")
    except ValueError:
        messagebox.showerror("Ingresa un número válido")

# Función para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)
    resultado.config(text="")
    mensaje.config(text="")

# Función para actualizar el historial
def actualizar_historial():
    historial_text.delete("1.0", tk.END)
    for i, (r, a, hora) in enumerate(historial):
        historial_text.insert(tk.END, f"{i+1} {hora} - Radio: {r}  Área: {a:.2f}\n")

# Estilo de etiquetas y botones
estilo_label = {"bg": "lightpink", "font": ("Arial", 12)}
estilo_titulo = {"bg": "blue", "font": ("Arial", 14, "bold")}

# Widgets
tk.Label(ventana, text="Ingresa el radio:", **estilo_label).pack(pady=5)
entrada = tk.Entry(ventana, font=("Arial", 12), justify="center")
entrada.pack(pady=5)

resultado = tk.Label(ventana, text="", font=("Arial", 13), bg="lightblue")
resultado.pack(pady=5)

mensaje = tk.Label(ventana, text="", font=("Arial", 13, "bold"), bg="lightblue")
mensaje.pack(pady=5)

total_label = tk.Label(ventana, text="Total de cálculos: 0", **estilo_label)
total_label.pack(pady=5)

tk.Label(ventana, text="Historial:", **estilo_titulo).pack(pady=5)
historial_text = tk.Text(ventana, height=10, width=45, bg="#ffffff", font=("Courier", 10))
historial_text.pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular_area, bg="#4fc3f7", fg="black",
          font=("Arial", 11), width=20).pack(pady=5)
tk.Button(ventana, text="Limpiar entrada", command=limpiar, bg="#b2ebf2", fg="black",
          font=("Arial", 11), width=20).pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()