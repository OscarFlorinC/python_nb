# Bucle For con listas
animales = ["gato", "perro", "serpiente"]
for animal in animales:
    print(f"El animal es: {animal}, tamaño de palabra es: {len(animal)}")



# Bucle For con listas y función "range"
oracion = "Mary entiende muy bien Python"
frases = oracion.split()  # convierte a una lista cada palabra
print("La oración analizada es:", oracion, ".\n")
for palabra in range(len(frases)):
    print(f"Palabra: {frases[palabra]}, en la frase su posición es: {palabra}")



# For con Tuplas 
conexion_bd = "127.0.0.1", "root", "123456", "nomina"
for parametro in conexion_bd:
    print(parametro)




# For Con Diccionarios
datos_basicos = {
    "nombres": "Leonardo Jose",
    "apellidos": "Caballero Garcia",
    "cedula": "26938401",
    "fecha_nacimiento": "03/12/1980",
    "lugar_nacimiento": "Maracaibo, Zulia, Venezuela",
    "nacionalidad": "Venezolana",
    "estado_civil": "Soltero",
}
clave = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print(clave + ": " + valor)



# For con else
db_connection = "127.0.0.1", "5432", "root", "nomina"
for parametro in db_connection:
    print(parametro)
else:
    print(
        """El comando PostgreSQL es:
$ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
            server=db_connection[0],
            port=db_connection[1],
            user=db_connection[2],
            db_name=db_connection[3],
        )
    )