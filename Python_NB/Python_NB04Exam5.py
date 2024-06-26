'''Ejercicio 2
Hacer un programa que pida al usuario su nombre, su edad y su 
sexo y los muestre de la siguiente forma:
Te llamas: <nombre>
Tu edad es: <edad>
Eres: <sexo>'''

nombre = input("Nombre: ")
edad = int(input("Edad: "))
sexo = input("Sexo: ")

#print("Te llamas: {}" "\nTu edad: {}" "\nEres: {}".format(nombre,edad,sexo)) #este es mio
print("Te llamas: {} \nTu edad: {} \nEres: {}".format(nombre,edad,sexo)) #clase
#print("Te llamas: {}".format(nombre))
#print("Tu edad: {}".format(edad))
#print("Eres: {}".format(sexo))