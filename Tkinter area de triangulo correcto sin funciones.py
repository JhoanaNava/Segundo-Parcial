import tkinter as tk
from tkinter import messagebox
import math

ventana = tk.Tk()
ventana.title("Área del Círculo")
ventana.geometry("300x200")
ventana.configure(bg="lightblue")

tk.Label(ventana, text="Ingresa el radio:", bg="pink").pack(pady=10)
entry_radio = tk.Entry(ventana)
entry_radio.pack()

resul = tk.Label(ventana, text="", bg="lightblue")
resul.pack()
comparacion = tk.Label(ventana, text="", bg="lightblue")
comparacion.pack()
comparacion2 = tk.Label(ventana, text="", bg="lightblue")
comparacion2.pack()

boton = tk.Button(ventana, text="Calcula", command=lambda: [
    resul.config(text=f"El área es: {math.pi * (float(entry_radio.get()) ** 2):.2f}") if entry_radio.get().replace('.', '', 1).isdigit() else resul.config(text="Por favor, ingresa un valor numérico"),
    comparacion.config(text="Area GRANDE") if entry_radio.get().replace('.', '', 1).isdigit() and math.pi * (float(entry_radio.get()) ** 2) > 100 else comparacion.config(text=""),
    comparacion2.config(text="Area PEQUEÑA") if entry_radio.get().replace('.', '', 1).isdigit() and math.pi * (float(entry_radio.get()) ** 2) <= 100 else comparacion2.config(text="")
])
boton.pack()

limpiar = tk.Button(ventana, text="Limpiar y repetir", command=lambda: [
    entry_radio.delete(0, tk.END),
    resul.config(text=""),
    comparacion.config(text=""),
    comparacion2.config(text="")
])
limpiar.pack()

ventana.mainloop()