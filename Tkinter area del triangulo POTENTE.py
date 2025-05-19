import tkinter as tk
import math
from datetime import datetime

ventana = tk.Tk()
ventana.title("Área del Círculo PRO")
ventana.geometry("420x460")
ventana.configure(bg="#e0f7fa")

resultados = []

tk.Label(ventana, text="Ingresa el radio:", bg="#b2ebf2", font=("Arial", 10)).pack(pady=5)
entry_radio = tk.Entry(ventana)
entry_radio.pack()

label_area = tk.Label(ventana, text="", bg="#e0f7fa", font=("Arial", 10))
label_area.pack(pady=5)

label_estado = tk.Label(ventana, text="", bg="#e0f7fa", font=("Arial", 10, "bold"))
label_estado.pack(pady=5)

label_total = tk.Label(ventana, text="Total de cálculos: 0", bg="#e0f7fa", font=("Arial", 10))
label_total.pack()

tk.Label(ventana, text="Historial:", bg="#e0f7fa", font=("Arial", 10, "underline")).pack(pady=10)
lista_resultados = tk.Text(ventana, height=12, width=55, bg="#ffffff", state="disabled", font=("Courier", 10))
lista_resultados.pack()

tk.Button(ventana, text="Calcular", bg="#00838f", fg="white", command=lambda: [
    (
        resultados.append(
            f"{datetime.now().strftime('%H:%M:%S')} - Radio: {entry_radio.get()} → Área: {math.pi * float(entry_radio.get()) ** 2:.2f}"
        ),
        label_area.config(text=f"El área es: {math.pi * float(entry_radio.get()) ** 2:.2f}"),
        label_estado.config(
            text="Área GRANDE" if math.pi * float(entry_radio.get()) ** 2 > 100 else "Área PEQUEÑA",
            fg="red" if math.pi * float(entry_radio.get()) ** 2 > 100 else "green"
        ),
        label_total.config(text=f"Total de cálculos: {len(resultados)}"),
        lista_resultados.config(state="normal"),
        lista_resultados.delete("1.0", tk.END),
        [lista_resultados.insert(tk.END, f"{i+1}. {res}\n") for i, res in enumerate(resultados)],
        lista_resultados.config(state="disabled")
    )
    if entry_radio.get().replace('.', '', 1).isdigit() and float(entry_radio.get()) > 0
    else (
        label_area.config(text="Ingresa un número válido mayor a 0"),
        label_estado.config(text="")
    )
]).pack(pady=5)

tk.Button(ventana, text="Limpiar entrada", command=lambda: [
    entry_radio.delete(0, tk.END),
    label_area.config(text=""),
    label_estado.config(text="")
]).pack(pady=5)
