#Ejercicio 1
print("Ejercicio 1")
numero_1=int(input("Ingrese el primer numero entero: "))
numero_2=int(input("Ingrese el segundo numero entero: "))
numero_3=int(input("Ingrese el tercer numero entero: "))
list_1=[numero_1,numero_2,numero_3]
list_1.sort()
print(list_1)
#Ejercicio 2
print("Ejercicio 2")
cadena=input("Ingrese una oracion en mayusculas: ")
cadena_minuscula=cadena.lower()
list_palabras_cadena=cadena_minuscula.split()
print(list_palabras_cadena)
