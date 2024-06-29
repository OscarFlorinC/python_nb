'''Ejercicio 1
Crear un programa que pida al usuario una letra, 
y si es vocal, muestre el mensaje "Es vocal". Sino, 
decirle al usuario que no es vocal
'''

letra = input("Escribe  una  letra: ")
#codigo clase
if letra.lower() in "aeiuo":
    print("Es una vocal y es la: " , letra)
else:
    print("No es una vocal es: " , letra)