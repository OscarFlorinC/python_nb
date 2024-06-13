'''Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:
• Imprima los dos primeros caracteres.
• Imprima los tres últimos caracteres.
• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca
• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh
• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''

cadena = "Te quiero solo como amigo"

print(cadena[ : 2])
print(cadena[21 : ]) # ó print(cadena[-3 : ])
print(cadena[: : 2])
print(cadena[: : -1])
print(cadena + cadena [:: -1])