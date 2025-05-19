import tkinter as tk
from tkinter import messagebox
import math

# Funciones de cálculo
def calcular_areas():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        lado = float(entry_lado.get())
        radio = float(entry_radio.get())

        area_triangulo = (base * altura) / 2
        area_rectangulo = base * altura
        area_cuadrado = lado * lado
        area_circulo = math.pi * (radio ** 2)

        label_resultado_triangulo.config(text=f"Área Triángulo: {area_triangulo:.2f}")
        label_resultado_rectangulo.config(text=f"Área Rectángulo: {area_rectangulo:.2f}")
        label_resultado_cuadrado.config(text=f"Área Cuadrado: {area_cuadrado:.2f}")
        label_resultado_circulo.config(text=f"Área Círculo: {area_circulo:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Áreas")
ventana.geometry("400x400")
ventana.configure(bg="#d0e1f9")  # Fondo azul claro

# Título
titulo = tk.Label(ventana, text="Cálculo de Áreas", font=("Helvetica", 16, "bold"), bg="#d0e1f9", fg="#2a4d69")
titulo.pack(pady=10)

# Entradas
frame_entradas = tk.Frame(ventana, bg="#d0e1f9")
frame_entradas.pack(pady=10)

tk.Label(frame_entradas, text="Base:", bg="#d0e1f9").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_base = tk.Entry(frame_entradas)
entry_base.grid(row=0, column=1)

tk.Label(frame_entradas, text="Altura:", bg="#d0e1f9").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_altura = tk.Entry(frame_entradas)
entry_altura.grid(row=1, column=1)

tk.Label(frame_entradas, text="Lado (cuadrado):", bg="#d0e1f9").grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry_lado = tk.Entry(frame_entradas)
entry_lado.grid(row=2, column=1)

tk.Label(frame_entradas, text="Radio (círculo):", bg="#d0e1f9").grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry_radio = tk.Entry(frame_entradas)
entry_radio.grid(row=3, column=1)

# Botón
btn_calcular = tk.Button(ventana, text="Calcular Áreas", command=calcular_areas, bg="#4a90e2", fg="white", font=("Helvetica", 12, "bold"))
btn_calcular.pack(pady=10)

# Resultados
frame_resultados = tk.Frame(ventana, bg="#d0e1f9")
frame_resultados.pack(pady=10)

label_resultado_triangulo = tk.Label(frame_resultados, text="Área Triángulo: ", bg="#d0e1f9")
label_resultado_triangulo.pack()

label_resultado_rectangulo = tk.Label(frame_resultados, text="Área Rectángulo: ", bg="#d0e1f9")
label_resultado_rectangulo.pack()

label_resultado_cuadrado = tk.Label(frame_resultados, text="Área Cuadrado: ", bg="#d0e1f9")
label_resultado_cuadrado.pack()

label_resultado_circulo = tk.Label(frame_resultados, text="Área Círculo: ", bg="#d0e1f9")
label_resultado_circulo.pack()

# Ejecutar ventana
ventana.mainloop()
