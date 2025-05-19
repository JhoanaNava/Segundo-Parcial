import tkinter as tk
from tkinter import messagebox

def calcular_area():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        area = (base * altura) / 2
        label_resultado.config(text=f"Área: {area}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Área de un Triángulo")

# Etiquetas y entradas
tk.Label(ventana, text="Base:").grid(row=0, column=0, padx=10, pady=5)
entry_base = tk.Entry(ventana)
entry_base.grid(row=0, column=1)

tk.Label(ventana, text="Altura:").grid(row=1, column=0, padx=10, pady=5)
entry_altura = tk.Entry(ventana)
entry_altura.grid(row=1, column=1)

# Botón de cálculo
tk.Button(ventana, text="Calcular Área", command=calcular_area).grid(row=2, column=0, columnspan=2, pady=10)

# Resultado
label_resultado = tk.Label(ventana, text="Área: ")
label_resultado.grid(row=3, column=0, columnspan=2)

# Ejecutar ventana
ventana.mainloop()
