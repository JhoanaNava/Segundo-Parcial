# Listas para guardar los datos
nombres = []
numeros = []
calificaciones = []
sexos = []


for i in range(3):
    print(f"Alumno {i+1}")
    nombre = input("Nombre: ")
    numero = int(input("Numero de alumno: "))
    calificacion = float(input("Calificación: "))
    sexo = input("Sexo (M/F): ")

   
    nombres.append(nombre)
    numeros.append(numero)
    calificaciones.append(calificacion)
    sexos.append(sexo)


print(" Datos Recolectados")
for i in range(3):
    print(f"Alumno {i+1}:")
    print(f"Nombre: {nombres[i]}")
    print(f"Numero de alumno: {numeros[i]}")
    print(f"Calificación: {calificaciones[i]}")
    print(f"Sexo: {sexos[i]}")
