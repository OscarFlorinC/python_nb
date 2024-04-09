# Metodo __init__
def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo


# Ejemplo 1 método __init__
class Persona:
    def __init__(self, cedula, nombre, apellido, sexo):
            #Constructor de clase Persona
            self.cedula = cedula
            self.nombre = nombre
            self.apellido = apellido
            self.sexo = sexo

    def imprimir(self):
        print("Cédula: ", self.cedula)
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Sexo: ", self.sexo)

persona1 = Persona("MX-13458796", "Juan", "López", "M")
persona1.imprimir()



""" 
# Ejemplo 1b método __init__, con ingreso de datos
class Persona:
    def __init__(self):
            #Constructor de clase Persona
            self.cedula = input("Ingrese su ID: ")
            self.nombre = input("Ingrese su nombre: ")
            self.apellido = input("Ingrese su apellido: ")
            self.sexo = input("Ingrese su sexo: ")

    def imprimir(self):
        print("Cedula: ", self.cedula)
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Sexo: ", self.sexo)

persona1 = Persona()
persona1.imprimir()
"""


""" 
# Ejemplo 3 método __init__
class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado:")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")


# bloque principal

empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
"""
