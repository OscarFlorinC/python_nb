# Ejemplo de variables
a = 12 # Esta es una variable de tipo entero (int)
x = 'C' # Esta es una variable de tipo cadena (str)
nombre = "Juan B" # Esta también es una variable tipo cadena (str)

print(f"Hola, soy {nombre} estoy en el equipo {x} tengo {a} años!")

# Los nombres de las variables pueden comenzar con una letra o un guion bajo:
x = False
_y = True

print(f"La variable 'x' tiene el valor: {x}, la variable '_y' tiene el valor: {_y}")

# Pueden estar formadas con letras, números y guiones bajos:
variable_1 = "Bose"

print(variable_1)

# Los variables no deben ser palabras reservadas del lenguaje
import keyword
print(keyword.kwlist)

# Los Nombres son case sensitive, es decir que distinguen mayúsculas y minúsculas:
x = 5
z = X + 20
print(z)
