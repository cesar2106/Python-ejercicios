### 
# 01_ sentencia condicionales  (if,elif. else)
# Permite ejecutar bloques de codigos  solo si se cumple ciertas condiciones 
##

# print ("\n Sentencia simple condicional") 

from os import system
if system("clear") != 0: system("cls")


edad = 17
if edad >= 18:
  print("Eres mayor de edad" + " felicidades")
  
else :
   print ("eres menor de edad" + " lo siento") 
   
# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del if

print("\n Sentencia condicional con elif")

nota = 6

if nota >= 9 :
  print("aprobado")
elif nota >= 7:
    print("sobresaliente")
elif nota <=6:
    print ("reprobado")
else :
    print ("no estas calificado")
    
    
    
print("\n Condiciones múltiples")
edad = 18
tiene_carnet = True

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript: 
# && sería and
# || sería or

# En el caso que seas mayor de edad y tengas carnet...
# entonces podrás conducir




if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")
  
  # En un pueblo de Isla Margarita son más laxos y
# te dejan conducir si eres mayor de edad O tienes carnet

if edad >= 18 or tiene_carnet:
    print("puede conducir")
else:
    print("realice el curso de conduccion")
    
 # También tenemos el operador lógico "not"
# que nos permite negar una condición
es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡cesar, venga que hay que streamear!")

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

# Más fácil sería:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
  print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
  print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
  print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)   
 
###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

usuario1 = input("Ingrese un numero \n")
usuario2 =input ("ingrese un numero \n ")

if usuario1 > usuario2:
    print ("el numeromayor es :" +  usuario1)
    
elif usuario2 > usuario1 :
     print("el numero mayor :" +  usuario2)
else:
    print("los numero son iguales")
    
    # Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)




num1=float(input("Ingrese un numero \n"))
num2=float(input ("ingrese otro numero \n "))

operacion =input("introduce la operacion(+,-,*./) : ")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.




# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Ingrese su edad\n"))

if edad <=0  and edad >=2:
    print ("es un bebe")
elif edad >=3 and edad <=12 :
    print ("es un niño")
elif edad >=13 and edad <=17:
    print("es adolecente")
elif edad >= 18 and  edad <=64 :
    print ("Adulto")
elif edad >= 65:
    print("adulto mayor")
    