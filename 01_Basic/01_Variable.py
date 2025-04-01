##
#01 - variables
# las variables sirve para guardar datos en memoria
# python es un lengiaje de tipa dinamico y de tipado fuerte.
###

# asignar una variable
# solo hace falta poner esto

#my_name = "ejercicios"

#print (my_name)

#age = 33

#age = 34 

#print (age)

 # la variable se puede reasignar o cambiar su valor
 
 # tipado dinamico:  el tipo de dato se determina en tiempo de ejecucion
 # que no tienes que declararlo explicitamente
 
#name = "cesar"

#print (type(name))

#name = 33

#print (type(name))

# tipado fuerte : python no realiza conversiones de tipo automatico 

# print (10 + "2")
#f-string (literal de cadena de  formato)
#desde  la version 3.6 esta disponible

#print (f"hola {my_name} , tengo {age} , años")

# no se recomienda  asignar variables de la siguiente forma

#name, age, city = "cesar", 33 , "cartagena"

# conversiones de nombre de variables

mi_nombre_de_variable = "ok" # snake_Case
nombre = "ok"

MiNombreDeVariable = "ko" # pascalcase
minombredevariable = "ko" # todojunto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # Python no tiene constantes

#upper_case se puede convertir  y reasignar.

# nombre  no validos de variables

#123123_variable = "ro"
#mi-variable = "ro"
# mi variable = "ro"  

# Palabras reservadas en Python (no se pueden usar como nombres de variables)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# Anotaciones de tipo (opcional, para mayor claridad en el código)
is_user_logged_in : bool =  True  # Indica que la variable es un booleano

print (is_user_logged_in)

is_user_logged_in = 42 

print (is_user_logged_in)

name: str = "cesar" # Indica que la variable es una cadena de texto
print(name)