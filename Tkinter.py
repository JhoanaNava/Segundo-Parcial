import tkinter as tk

def saludar():
 nombre = entrada.get()
 edad = entrada_edad.get()
 etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad} años.")
 
ventana = tk.Tk()
ventana.title("Mi primera app gráfica")
ventana.geometry("500x300")

ventana.config(bg="cornsilk")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:", bg="thistle")
etiqueta.pack()
entrada = tk.Entry(ventana)
entrada.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:", bg="thistle")
etiqueta_edad.pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar Saludo", command=saludar)
boton.pack()


etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

etiqueta_autor = tk.Label(ventana, text="Autor: Jhoana Nava Bautista", bg="thistle", font=("Helvetica", 10, "italic"))
etiqueta_autor.pack(side="bottom", pady=5)

ventana.mainloop()
