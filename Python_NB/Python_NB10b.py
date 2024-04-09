""" 
# Ejemplo métodos
class Persona:
    #Clase que representa una Persona

    cedula = "MX-26938401"
    nombre = "Juan"
    apellido = "López"
    sexo = "M"

    def hablar(self, mensaje):
        #Mostrar mensaje de saludo de Persona
        return mensaje

texca = Persona
print("El objeto de la clase {}, {}.".format(texca.__name__, texca.__doc__))
print("Hola, mucho gusto, mi nombre es '{} {}', \nmi cédula de identidad es '{}', y mi sexo es '{}'.".format(
    texca.nombre,
    texca.apellido,
    texca.cedula,
    texca.sexo)
)
"""
""" 
# Ejemplo métodos
class Persona:
    #Clase que representa una Persona

    cedula = "MX-26938401"
    nombre = "Juan"
    apellido = "López"
    sexo = "M"

    def hablar(self, mensaje):
        # Mostrar mensaje de saludo de Persona
        return mensaje

texca = Persona
print(type(Persona()))
print(Persona().__doc__)
print(Persona().hablar.__doc__)
print(type(Persona().hablar))
print(Persona().hablar.__doc__)
print(Persona().hablar("Hola soy la clase {0}.".format(texca.__class__.__name__)))

"""

""" 
# Estructura de Método de clase
class <Clase>:
    # Linea 1 de Código
    # Linea 2 de Código
    .
    .
    .
    @classmethod
    def <metodo>(cls, <argumentos>):
            # Linea 1 de Código
            # Linea 2 de Código
            .
            .

"""

""" 
# Estructura de Método estáticos
class <Clase>:
    # Linea 1 de Código
    # Linea 2 de Código
    .
    .
    .
    @staticmethod
    def <metodo>(<argumentos>):
            # Linea 1 de Código
            # Linea 2 de Código
            .
            .

"""


# Instancias
persona1 = Persona("MX-13458796", "Juan", "López", "M")
print(persona1)

