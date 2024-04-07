""" 
# Ejemplo de POO
class Persona:
    #Clase que representa una Persona
    cedula = "MX-26938401"
    nombre = "Juan"
    apellido = "López"
    sexo = "M"

texca = Persona
print(type(texca))
print(dir(texca))
print(texca.cedula)
print(texca.nombre)
print(texca.apellido)
print(texca.sexo)

print("El objeto de la clase {}, {}.".format(texca.__name__, texca.__doc__))
print("Hola, mucho gusto, mi nombre es '{} {}', \nmi cédula de identidad es '{}', y mi sexo es '{}'.".format(
    texca.nombre,
    texca.apellido,
    texca.cedula,
    texca.sexo)
    )
"""

# Ejemplo de POO
class Persona:
    #Clase que representa una Persona
    cedula = "MX-26938401"
    nombre = "Juan"
    apellido = "López"
    sexo = "M"

texca = Persona

print(texca.__name__)
print(texca.__doc__)
