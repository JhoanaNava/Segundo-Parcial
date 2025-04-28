num1=float(input("ingresa el primer numero: "))
num2=float(input("ingresa el segundo numero: "))
print("operaciones disonibles:")
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
opcion=(input)("Elija una opcion")
if opcion=='1':
   resultado=num1+num2
   int=resultado
   print(f"la suma es:{resultado}")
elif opcion=='2':
   resultado=num1-num2
   print(f"la resta es:{resultado}")
elif opcion=='3':
   resultado=num1*num2
   print(f"la multiplicacion es:{resultado}")
elif opcion=='4':
    if num2!=0:
    
     resultado=num1/num2
     int=resultado
     print(f"la division es:{resultado}")
    else:
     print("Error")
else: 
    print("Operacion no valida")
    

        