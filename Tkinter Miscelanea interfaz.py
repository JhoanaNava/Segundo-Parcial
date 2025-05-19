import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

datos = []

def Bienvenida():
    Borrar()
    tk.Label(area_dinamica, text="Aquí va un mensaje de bienvenida", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida:", command=lambda: messagebox.showinfo("Título", "Bienvenido a este programa")).pack()

def Identificador():
    Borrar()
    tk.Label(area_dinamica, text="Aquí coloca un letrero o label que identifique al alumno", font=("Arial", 14)).pack(pady=10)#colocamos nuevo letrero 

    tk.Label(area_dinamica, text="Nombre del alumno:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="opcion A:").pack()
    opcion_elegida = tk.StringVar(value="Opción 1")
    tk.Radiobutton(area_dinamica, text="Opción 1", variable=opcion_elegida, value="Opción 1").pack()
    tk.Radiobutton(area_dinamica, text="Opción 2", variable=opcion_elegida, value="Opción 2").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    combo.pack()
    combo.current(0)

    etiqueta_datos = tk.Label(area_dinamica, text="", font=("Arial", 12), fg="blue") 
    etiqueta_datos.pack(pady=10)
    
    
    def Guardar():
        valor = campo_texto_uno.get()
        seleccion = opcion_elegida.get()
        lista = combo.get()
        
        
        datos.append(f"Nombre: {valor}, Selección: {seleccion}, Lista: {lista}")
        
        
        etiqueta_datos.config(text="\n".join(datos))
 
        messagebox.showinfo("Datos del usuario", f"Texto: {valor}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")

    tk.Button(area_dinamica, text="mostrar datos", command=Guardar).pack(pady=10) 

def Color():
    Borrar ()
    tk.Label(area_dinamica, text="Cambia el color", font=("Arial", 14)).pack(pady=10) 

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack() 

    def diferente_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: diferente_color(col)).pack(pady=2)

def Cuestionario():
    Borrar ()
    tk.Label(area_dinamica, text="Explicacion del alumno", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def Borrar ():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")


tk.Button(menu_lateral, text="Inicio:", command=Bienvenida, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Mostrar datos", command=Identificador, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Colores", command= Color, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Cuestionario", command=Cuestionario, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

Bienvenida()
ventana_principal.mainloop()



