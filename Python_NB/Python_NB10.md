# ***Programación orientada a objetos***
<img src="../imagenes/15.-PyOOP.png" width="700" height="300">

##### - ***Imagen de Real Python***

### La programación orientada a objetos (POO, u OOP según sus siglas en inglés) es un paradigma de programación que viene a innovar la forma de obtener resultados. Los objetos manipulan los datos de entrada para la obtención de datos de salida específicos, donde cada objeto ofrece una funcionalidad especial.

### Muchos de los objetos prediseñados de los lenguajes de programación actuales permiten la agrupación en bibliotecas o librerías, sin embargo, muchos de estos lenguajes permiten al usuario la creación de sus propias bibliotecas.

# POO en Python

### En Python las clases es una mezcla de los mecanismos de clase encontrados en C++ y Modula-3.

### Como es cierto para los módulos, las clases en Python no ponen una barrera absoluta entre la definición y el usuario, sino que más bien se apoya en la cortesía del usuario de no «forzar la definición».

### Se mantiene el poder completo de las características más importantes de las clases: el mecanismo de la herencia de clases permite múltiples clases base, una clase derivada puede sobrescribir cualquier método de su(s) clase(s) base, y un método puede llamar al método de la clase base con el mismo nombre.

    «Los objetos pueden tener una cantidad arbitraria de datos.»

### En terminología de C++, todos los miembros de las clases (incluyendo los miembros de datos), son públicos, y todas las funciones miembro son virtuales.

### Como en Modula-3, no hay atajos para hacer referencia a los miembros del objeto desde sus métodos: la función método se declara con un primer argumento explícito que representa al objeto, el cual se provee implícitamente por la llamada.


### Algunas particularidades de POO en Python son las siguientes:

- Todo es un objeto, incluyendo los tipos y clases.
- Permite herencia múltiple.
- No existen métodos ni atributos privados.
- Los atributos pueden ser modificados directamente.
- Permite «monkey patching».
- Permite «duck typing».
- Permite la sobrecarga de operadores.
- Permite la creación de nuevos tipos de datos.


# ***Objetos***

### Los objetos son abstracción de Python para data. Toda la data en un programa Python es representado por objectos o por relaciones entre objectos.

### Cada objeto tiene una identidad, un tipo y un valor. Una identidad de objecto nunca cambia una vez que es creada; usted puede pensar eso como la dirección de objeto en memoria. El operador in compara la identidad de dos objetos; la función id() devuelve un número entero representando la identidad (actualmente implementado como su dirección).

### El tipo de un objeto también es inmutable. El tipo de un objeto determina las operaciones que admite el objeto (por ejemplo, «¿tiene una longitud?») Y también define los valores posibles para los objetos de ese tipo. La función ***«type()»*** devuelve el tipo de un objeto (que es un objeto en sí mismo). El valor de algunos objetos puede cambiar. Se dice que los objetos cuyo valor puede cambiar son mutables; los objetos cuyo valor no se puede cambiar una vez que se crean se llaman immutable. La mutabilidad de un objeto está determinada por su tipo.

### Los objetos son la clave para entender la POO. Si mira a nuestro alrededor encontrará un sin fin de objetos de la vida real: perro, escritorio, televisor, bicicleta, etc…

### En Python puede definir una clase con la palabra reservada class, de la siguiente forma:

<img src="../imagenes/15.-PycdPOO1.png" width="200" height="100">

### Salida: 
- /usr/local/bin/python3 /Users/juanlopez/Desktop/GitHub/Python_Basic/Python_NB/Python_NB10.py

### En el ejemplo anterior, el nombre de la clase es Persona y dentro del bloque de código usa la sentencia pass. La sentencia pass no es requerido por el intérprete, los nombres de las clases se escriben por convención capitalizadas. Las clases pueden (y siempre deberían) tener comentarios.

<img src="https://entrenamiento-python-basico.readthedocs.io/es/3.7/_images/poo_objetos_clases.png" width="250" height="200">

##### Diagrama de Objeto Persona

# Atributos

### Los atributos o propiedades de los objetos son las características que puede tener un objeto, como el color. Si el objeto es Persona, los atributos podrían ser: cedula, nombre, apellido, sexo, etc…

### Los atributos describen el estado de un objeto. Pueden ser de cualquier tipo de dato.

<img src="../imagenes/15.-PycdPOO2.png" width="400" height="200">

### Salida:
- <class '__main__.Persona'>

### Puedes probar el código anterior, si lo transcribe en el consola interactiva Python como lo siguiente:

<img src="../imagenes/15.-PycdPOO3.png" width="600" height="500">

### Salida:
- MX-26938401
- Juan
- López
- M
- El objeto de la clase Persona, None.
- Hola, mucho gusto, mi nombre es 'Juan López', 
- mi cédula de identidad es 'MX-26938401', y mi sexo es 'M'.

#
|  | Descripción |
|-----:|---------------|
| [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion1/index.html#) | ***Documentación oficial*** |
| [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](../README.md) | ***Inicio del curso*** |

## Puedes seguir y apoyar mi trabajo haciendo click en "☆ Star" y en el botón de Follow.
## ¡Muchas gracias, bienvenido!!!

## Contacto y apoyo:

<br>[![LinkedIn](https://img.shields.io/badge/Oscar_Florin-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/oscarflorincontreras)
[![X](https://img.shields.io/badge/DevozzCloud-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/DevozzCloud)</br>
[![Just_Eat](https://img.shields.io/badge/🌮_Donaciones_para_tacos-7A1FA2?style=for-the-badge&logo=)](https://paypal.me/OscarFlorin?country.x=MX&locale.x=es_XC)
[![Eats](https://img.shields.io/badge/🐈_Donaciones_para_gatos-black?style=for-the-badge&logo=)](https://paypal.me/OscarFlorin?country.x=MX&locale.x=es_XC)
