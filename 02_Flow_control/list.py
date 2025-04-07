###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")


# cracion de lista

print("\ncrear listas")
list1 = [1,2,3,4,5] # list ade enteros
list2 = ["manzana", "Peras", "platanos"] #Lista de cadena de texto
list3 = [1, "hola", 3.14, True] # listo de tipos mixtos 

lista_vacia = []

lista_de_listas = [[1,2],[3,4] ]
matrix = [[1,2],[2,3], [4,4]]

print (list1)
print(list2)
print(list3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

 #acceso a elementos por indices
 
print("\nacceso a elementos por indices")

print(list2[1]) # en programacion la posicion # 0 es la posicion # 1

# si quieres acceder a la ultima posicion y no la sabes podemos usar la posicion -1

print(list2[-1])
print(list3[-1])

# como acceder en una lista de lista

print(lista_de_listas[1][0])

#(slicing) esta funcion te permite recorrer la lista des una posicion inicial hasta la que determines
#y te permite modificarla

print(list1[1:4])

print(list1[:3])

print(list1[3:])

print(list1[:]) # te crea una copia de  la lista

#  hay mas

# print(list1[desde:hasta:paso]) ##


lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares
print(lista1[::-1]) # para devolver índices inversos

# Modificar listas

lista1 [1]= 30
print(lista1)

# añadir elementos a una lista

lista1 = [1, 2, 3]

#formas larga y menos eficiente

lista1 = lista1 + [7, 8, 9]
print (lista1)

# formas cortas y mas eficiente

lista1 += [8, 9, 10]
print(lista1)

# recuperar la longitud de una lista

print("recuperar la longitud de la lista", len(list1))



###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje  = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

mensaje = ["el mensaje secreto"]

print(mensaje)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

numero = [10, 20, 30, 40, 50]

numero [0] = 50 
numero [4] = 10

print(numero[0], numero[4])
print (numero)


# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.


pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = [pan, ingredientes, pan_abajo]
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]

lista += [1, 2, 3]
print(lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50]

print(lista[2])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]


lista = [1, 2, 3, 4, 5, 6]

mitad = len(lista) // 2
lista_invertida = lista[:mitad][::-1] + lista[mitad:]

print(lista_invertida)

