""" 
# Error de sintaxis
while True print('Hola Mundo')
"""

# Excepciones
#10 * (1/0)
#4 + leonardo * 3
#"2" + 2

# Ejemplo manejando excepciones
while True:
    try:
        x = int(input("Por favor ingrese un número: "))
        break
    except ValueError:
        print("¡Oops!  No era válido. Intente nuevamente...")