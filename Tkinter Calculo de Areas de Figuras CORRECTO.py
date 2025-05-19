import tkinter as tk
import math

datos = []  

def Borrar():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

def actualizar_historial_en_area(etiqueta):
    historial = "\n".join(f"{i+1}. {d}" for i, d in enumerate(datos))
    etiqueta.config(text=historial)

def AreaCuadrado():
    Borrar()
    tk.Label(area_dinamica, text="Área del Cuadrado", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Lado:").pack()
    entrada = tk.Entry(area_dinamica)
    entrada.pack(pady=5)

    historial_label = tk.Label(area_dinamica, text="", fg="blue", justify="left", anchor="w")
    historial_label.pack(pady=10)

    actualizar_historial_en_area(historial_label)

    def calcular():
            lado = float(entrada.get())
            area = lado ** 2
            resultado = f"Cuadrado - Lado: {lado}, Área: {area:.2f}"
            datos.append(resultado)
            actualizar_historial_en_area(historial_label)
  

    tk.Button(area_dinamica, text="Calcular", command=calcular).pack(pady=10)

def AreaTriangulo():
    Borrar()
    tk.Label(area_dinamica, text="Área del Triángulo", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Base:").pack()
    base = tk.Entry(area_dinamica)
    base.pack(pady=5)

    tk.Label(area_dinamica, text="Altura:").pack()
    altura = tk.Entry(area_dinamica)
    altura.pack(pady=5)

    historial_label = tk.Label(area_dinamica, text="", fg="blue", justify="left", anchor="w")
    historial_label.pack(pady=10)

    actualizar_historial_en_area(historial_label)

    def calcular():
            b = float(base.get())
            h = float(altura.get())
            area = (b * h) / 2
            resultado = f"Triángulo - Base: {b}, Altura: {h}, Área: {area:.2f}"
            datos.append(resultado)
            actualizar_historial_en_area(historial_label)
 

    tk.Button(area_dinamica, text="Calcular", command=calcular).pack(pady=10)

def AreaCirculo():
    Borrar()
    tk.Label(area_dinamica, text="Área del Círculo", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Radio:").pack()
    radio = tk.Entry(area_dinamica)
    radio.pack(pady=5)

    historial_label = tk.Label(area_dinamica, text="", fg="blue", justify="left", anchor="w")
    historial_label.pack(pady=10)

    actualizar_historial_en_area(historial_label)

    def calcular():
            r = float(radio.get())
            area = math.pi * r ** 2
            resultado = f"Círculo - Radio: {r}, Área: {area:.2f}"
            datos.append(resultado)
            actualizar_historial_en_area(historial_label)
    

    tk.Button(area_dinamica, text="Calcular", command=calcular).pack(pady=10)

def AreaRectangulo():
    Borrar()
    tk.Label(area_dinamica, text="Área del Rectángulo", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Base:").pack()
    base = tk.Entry(area_dinamica)
    base.pack(pady=5)

    tk.Label(area_dinamica, text="Altura:").pack()
    altura = tk.Entry(area_dinamica)
    altura.pack(pady=5)

    historial_label = tk.Label(area_dinamica, text="", fg="blue", justify="left", anchor="w")
    historial_label.pack(pady=10)

    actualizar_historial_en_area(historial_label)

    def calcular():
            b = float(base.get())
            h = float(altura.get())
            area = b * h
            resultado = f"Rectángulo - Base: {b}, Altura: {h}, Área: {area:.2f}"
            datos.append(resultado)
            actualizar_historial_en_area(historial_label)

    tk.Button(area_dinamica, text="Calcular", command=calcular).pack(pady=10)

ventana_principal = tk.Tk()
ventana_principal.title("Áreas de Figuras")
ventana_principal.geometry("600x400")
ventana_principal.config(bg="lightblue")


menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=150)
menu_lateral.pack(side="left", fill="y")


area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")


tk.Button(menu_lateral, text="Cuadrado", command=AreaCuadrado, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Triángulo", command=AreaTriangulo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Círculo", command=AreaCirculo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Rectángulo", command=AreaRectangulo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

ventana_principal.mainloop()
