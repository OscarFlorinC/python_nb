'''Ejercicio 2
Crear un programa que permita al usuario elegir un candidato por 
el cual votar. Las posibilidades son: candidato A por el partido 
rojo, candidato B por el partido verde, candidato C por el partido 
azul. Según el candidato elegido (A, B ó C) se le debe imprimir el 
mensaje “Usted ha votado por el partido [color que corresponda al 
candidato elegido]”. Si el usuario ingresa una opción que no 
corresponde a ninguno de los candidatos disponibles, indicar 
“Opción errónea”.
Pista: Si la letra ingresada por el usuario es en minúscula, el 
programa debe convertirla en mayúscula'''

candidato = input("Por cual candidato votas (A), (B) ó (C): ")

if candidato.upper() == "A":
    print("Votaste por el partido Rojo")
elif candidato.upper() == "B":
    print("Votaste por el partido Verde")
elif candidato.upper() == "C":
    print("Votaste por el partido Azul")
else:
    print("No votaste por nadie")