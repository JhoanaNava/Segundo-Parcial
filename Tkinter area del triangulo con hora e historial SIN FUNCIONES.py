import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import math

ventana = tk.Tk()
ventana.title("Área del Círculo PRO")
ventana.geometry("420x500")
ventana.configure(bg="#e0f7fa")

contador = 0
historial = []

# Etiquetas y entrada
tk.Label(ventana, text="Ingresa el radio:", bg="#e0f7fa", font=("Arial", 12)).pack(pady=5)
entrada = tk.Entry(ventana, font=("Arial", 12), justify="center")
entrada.pack(pady=5)

resultado = tk.Label(ventana, text="", font=("Arial", 13), bg="#e0f7fa")
resultado.pack(pady=5)

mensaje = tk.Label(ventana, text="", font=("Arial", 13, "bold"), bg="#e0f7fa")
mensaje.pack(pady=5)

total_label = tk.Label(ventana, text="Total de cálculos: 0", bg="#e0f7fa", font=("Arial", 12))
total_label.pack(pady=5)

tk.Label(ventana, text="Historial:", bg="#e0f7fa", font=("Arial", 14, "bold")).pack(pady=5)
historial_text = tk.Text(ventana, height=10, width=45, bg="#ffffff", font=("Courier", 10))
historial_text.pack(pady=5)

# Botón calcular 
tk.Button(
    ventana,
    text="Calcular",
    bg="#4fc3f7",
    fg="black",
    font=("Arial", 11),
    width=20,
    command=lambda: (
        entrada.get().replace(",", "."),
        globals().update(contador=contador + 1),
        resultado.config(text=""),
        mensaje.config(text=""),
        (
            lambda r=entrada.get(): (
                (
                    float(r),
                    math.pi * float(r) ** 2,
                    datetime.now().strftime("%H:%M:%S")
                ) if r else (_ for _ in ()).throw(ValueError)
            )
        )(),
        globals().update(radio=float(entrada.get())),
        globals().update(area=math.pi * radio ** 2),
        resultado.config(text=f"El área es: {area:.2f}"),
        mensaje.config(
            text="Área GRANDE" if area > 100 else "Área PEQUEÑA",
            fg="#d32f2f" if area > 100 else "#388e3c"
        ),
        historial.append((radio, area, datetime.now().strftime("%H:%M:%S"))),
        historial_text.delete("1.0", tk.END),
        [historial_text.insert(tk.END, f"{i+1}. {h} - Radio: {r}  Área: {a:.2f}\n")
         for i, (r, a, h) in enumerate(historial)],
        total_label.config(text=f"Total de cálculos: {len(historial)}")
    ) if entrada.get() else messagebox.showerror("Error", "Ingresa un número válido")
).pack(pady=5)

# Botón limpiar 
tk.Button(
    ventana,
    text="Limpiar entrada",
    bg="#b2ebf2",
    fg="black",
    font=("Arial", 11),
    width=20,
    command=lambda: (
        entrada.delete(0, tk.END),
        resultado.config(text=""),
        mensaje.config(text="")
    )
).pack(pady=5)

ventana.mainloop()