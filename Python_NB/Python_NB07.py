# Bucle While
suma, numero = 0, 1

while numero <= 10:
    suma = numero + suma
    numero = numero + 1
print("La suma es " + str(suma))


# While con else
promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

grado = int(input(mensaje))
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print("Promedio de notas del grado escolar: " + str(promedio))


# While con break
variable = 10

while variable > 0:
    print("Actual valor de variable:", variable)
    variable = variable - 1
    if variable == 5:
        break

# While con Continue
variable = 10

while variable > 0:
    variable = variable - 1
    if variable == 5:
        continue
    print("Actual valor de variable:", variable)

