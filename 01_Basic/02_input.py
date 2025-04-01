###
# 02 - entrada de usuario (input()) - Version
#simplificada
# la funcion de input () permite obtener datos del usuario a traves de la consola
###

nombre = input(("hola, ¿ como te llamas?\n"))
print (f"hola {nombre}, encantado de conocerte")

age = input("cuantos años tienes?\n")
age = int(age) # se convierte la edad en un numero entero

print (f"dentro de 20 años tendras { age + 20 }")  

print ("obtener multiples valores a la vez ")

country , city = input ("¿en que pais y ciudad vives?\n") .split()  # el split recupera la cadena de texto y las separadas

print (f"vives en {country}, {city}")


