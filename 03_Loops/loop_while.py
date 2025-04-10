###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###



# Bucle  con una simple condicion



#while contador <= 5 :
   # print(contador)
    #contador += 1 # esto es super importante para evitar bucles infinitos
 # utilizando la palabra break, para romper el bucle   
 
print("\n Bucle while con break")
contador = 0

while True:
    print(contador) 
    contador +=1
    if contador == 5 :
        break # salida del bucle
    
 # continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\n Bucle con continue")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue

  print(contador) 
  
#else esta condicion  cuando se ejecuta

print("\n Bucle con else")

contador = 0
while contador <= 5:
   print(contador)
   contador += 1
else:
 print("El bucle ha terminado")
 
 #pedirle al usuario un _# que tiene que ser positivo si no se le deja en paz
 
 #numero = -1
 
#while numero < 0:
 #numero =int(input("Escribe un numero positivo: "))
#if numero < 0:
 #   print("el numero debe ser positivo para continuar")
    
#print(f"el numero que has introducido es {numero}")
 
#numero = -1
#while numero < 0:
  #ry:
   # numero = int(input("Escribe un número positivo: "))
    #if numero < 0:
     # print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  #except:
   # print("Lo que introduces debe ser un número,!")

#print(f"El número que has introducido es {numero}")
    
    
    ###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

numero  = 10 

while numero >= 1:
  print(numero)
  numero -=1 




# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

numero =1
sumas_pares = 0
while numero <= 20:
    if numero % 2 == 0:
        sumas_pares += numero
    numero += 1
    

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("Introduce un número entero positivo para calcular su factorial: "))
factorial = 1 # Inicializamos el factorial en 1
contador = 1 # Inicializamos el contador en 

while contador <= numero:
    factorial *= contador # Multiplicamos el factorial por el contador
    contador += 1 # Incrementamos el contador en 1  
    print(f"El factorial de {numero} es: {factorial}") # Imprimimos el resultado


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

contraseña = input("Introduce una contraseña (mínimo 8 caracteres): ")
while len(contraseña) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
    contraseña = input("Introduce una contraseña (mínimo 8 caracteres): ")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

numero = int(input("Introduce un número entero positivo N: "))    
while numero < 2:
    print("El número debe ser mayor o igual a 2.")
    numero = int(input("Introduce un número entero positivo N: "))