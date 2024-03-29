""" 
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("¡Boooooooom!")
    print("Fin de la función", numero)

cuenta_regresiva(5)
 """

""" 
# Funcion Recursiva con retorno
def factorial(numero):
    print("Valor inicial ->", numero)
    if numero > 1:
        numero = numero * factorial(numero - 1)
    print("valor final ->", numero)
    return numero

print(factorial(5))

 """

""" 
# Generadores
def gen_basico():
    yield "uno"
    yield "dos"
    yield "tres"
for valor in gen_basico():
    print(valor)

 """


# --------Decoradores-----------
# Declaramos funciones
def nuevo_decorador(function):
    def envuelve_la_funcion():
        print("Haciendo algo antes de llamar a function()")
        function()
        print("Haciendo algo despues de llamar a function()")
    return envuelve_la_funcion

# Aplicamos el decorador
@nuevo_decorador
def funcion_a_decorar():
    print("Soy la funcion que necesita ser decorada")

funcion_a_decorar()
funcion_a_decorar = nuevo_decorador(funcion_a_decorar)
funcion_a_decorar

 