import tkinter as tk

def sumar():
 
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado.config(text=f"Resultado de la suma: {num1+num2}")

    
   
def restar():

    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado.config(text=f"Resultado de la resta: {num1-num2}")
 
ventana = tk.Tk()
ventana.title("Suma y Resta")
ventana.geometry("500x300")

ventana.config(bg="cornsilk")

etiqueta1 = tk.Label(ventana, text="Ingresa el numero 1:", bg="thistle")
etiqueta1.pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

etiqueta2 = tk.Label(ventana, text="Ingresa el numero 2:", bg="thistle")
etiqueta2.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Suma", command=sumar)
boton.pack()



boton = tk.Button(ventana, text="Resta", command=restar)
boton.pack()



resultado = tk.Label(ventana, text="")
resultado.pack()

etiqueta_autor = tk.Label(ventana, text="Autor: Jhoana Nava Bautista", bg="thistle", font=("Helvetica", 10, "italic"))
etiqueta_autor.pack(side="bottom", pady=5)

ventana.mainloop()