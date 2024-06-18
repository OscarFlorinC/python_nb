'''Realizar un programa que haga el proceso de formula general para 
la resolución de ecuaciones, sabiendo que la formula general es la que
 está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, 
 y el programa debe hacer el proceso para que al final muestre el mensaje: 
 “La solución es: <solucion>”'''
#x=(-b +- ((b**2)-(4ac))^1/2) / 2*a
#3x^2-5x+2=0    x=1 , x=2/3
from math import sqrt #sqrt nos ayuda con la operacion raiz cuadrada

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))
x1 = 0
x2 = 0

if ((b**2) - (4*a*c)) < 0:
    print("no se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-b + sqrt((b**2) - (4*a*c))) / (2*a)
    x2 = (-b - sqrt((b**2) - (4*a*c))) / (2*a)
    print("La solucion es: \nx1= "  , x1 , "\nx1= " , x2)