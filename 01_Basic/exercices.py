###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

#print("\nEjercicio 1: Imprimir mensajes")
#print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
#name ,  city  = input ("cual es tu nombre y tu ciudad?\n") .split ()


#print(f"Mi nombre y ciudad es: {name} , {city}")


print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")

#a = 15
#b = 3.14159
#c = "Hola mundo"
#d = True
#e = None

### Completa aquí

#print(type(a))
#print (type(b))
#print(type(c))
#print (type(d))
#print(type(e))

###Ejercicio 3

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

#print(int("12345"))
#print(float("12345"))
#print(int(3.99))

### Ejercicio 4

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre = "cesar"
age = 39
altura = 1.72

print(f"hola! me llamo: " + (nombre) , "tengo " + str(age) , "y mido " + str(altura))


### Ejercicio 5

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")


import math

pi = math.pi 


print (round(pi) // 2)