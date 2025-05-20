import tkinter as tk


numeros = []
nombres = []
sexos = []
calificaciones = []

def guardar():
        numero = int(entry_numero.get())
        nombre = entry_nombre.get()
        sexo = entry_sexo.get()
        calificacion = float(entry_calificacion.get())


    
        numeros.append(numero)
        nombres.append(nombre)
        sexos.append(sexo)
        calificaciones.append(calificacion)

       
        entry_numero.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_sexo.delete(0, tk.END)
        entry_calificacion.delete(0, tk.END)

       
        if len(numeros) == 3:
            mostrar()



def mostrar():
    texto = "Estudiantes ingresados:\n"
    for i in range(3):
        texto += f"{i+1}. Número: {numeros[i]}, Nombre: {nombres[i]}, Sexo: {sexos[i]}, Calificación: {calificaciones[i]}\n"
    resultado.config(text=texto)


ventana = tk.Tk()
ventana.title("Registro de 3 Estudiantes")

tk.Label(ventana, text="Número de estudiante:", bg="lightblue").pack()
entry_numero = tk.Entry(ventana)
entry_numero.pack()

tk.Label(ventana, text="Nombre:", bg="lightblue").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Sexo (M/F):", bg="lightblue").pack()
entry_sexo = tk.Entry(ventana)
entry_sexo.pack()

tk.Label(ventana, text="Calificación:", bg="lightblue").pack()
entry_calificacion = tk.Entry(ventana)
entry_calificacion.pack()

tk.Button(ventana, text="Guardar", command=guardar).pack()

resultado = tk.Label(ventana, text="", justify="left", bg="lightblue")
resultado.pack()

ventana.mainloop()