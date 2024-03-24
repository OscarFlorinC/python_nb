""" # Ejemplo Fun
def hola(arg):
    #El docstring de la función
    print(f"¡Hola {arg}!")

hola("Plone") """

"""
# Función por posición  
def resta(a,b):
    print(a - b)

resta(30,10)

# Función por Nombre
def resta(a, b):
    print(a - b)

resta(b=30, a=10)
"""

"""
# Lambda Ejemplo:
def doblar(numero):
    resultado = numero * 2
    print(resultado)

doblar(2)
print(type(doblar))

# Lambda Ejemplo S1:
def doblar(numero):
    print(numero * 2)

doblar(2)
print(type(doblar))
"""
""" 
# Lambda Ejemplo S2:
def doblar(numero):
    print(numero * 2)

doblar(2)
print(type(doblar))
"""
""" 
# Lambda Ejemplo S2:
doblar = lambda numero: numero * 2
print(doblar)
"""

# Lambda Ejemplo F:
doblar = lambda numero: numero * 2
print(doblar(2))

print(type(doblar))

