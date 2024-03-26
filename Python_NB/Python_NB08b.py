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

# Funcion Recursiva con retorno
def factorial(numero):
    print("Valor inicial ->", numero)
    if numero > 1:
        numero = numero * factorial(numero - 1)
    print("valor final ->", numero)
    return numero

print(factorial(5))