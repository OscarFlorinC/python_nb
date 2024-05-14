# ***Programación estructurada***
<img src="../imagenes/13.-Funciones-en-Python_Estructura-de-una-función.png" width="600" height="400">

### La programación estructurada es un paradigma de programación basado en utilizar ***funciones*** o subrutinas, y únicamente tres estructuras de control:

- Secuencia: ejecución de una sentencia tras otra.
- Selección o condicional: ejecución de una sentencia o conjunto de sentencias, según el valor de una variable booleana.
- Iteración (ciclo o bucle): ejecución de una sentencia o conjunto de sentencias, mientras una variable booleana sea verdadera.

### Este paradigma se fundamenta en el teorema correspondiente, que establece que "toda función computable puede ser implementada en un lenguaje de programación que combine sólo estas tres estructuras lógicas o de control".

### La estructura de secuencia es la que se da naturalmente en el lenguaje, ya que por defecto las sentencias son ejecutadas en el orden en que aparecen escritas en el programa.

### Para las estructuras condicionales o de selección, Python dispone de la sentencia if, que puede combinarse con sentencias elif y/o else.

### Para los bucles o iteraciones existen las estructuras while y for.


# ***Funciones***
### Una función es un bloque de código con un nombre asociado, que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias, la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea, este bloque puede ser llamados cuando se necesite.

### El uso de funciones es un componente muy importante del paradigma de la programación llamada estructurada, y tiene varias ventajas:
- modularización: permite segmentar un programa complejo en una serie de partes o módulos más simples, facilitando así la programación y el depurado.
- reutilización: permite reutilizar una misma función en distintos programas.

### Python dispone de una serie de funciones integradas al lenguaje, y también permite crear funciones definidas por el usuario para ser usadas en su propios programas.

# Sentencia ***def***

### La sentencia def es una definición de función usada para crear objetos funciones definidas por el usuario.

### Una definición de función es una sentencia ejecutable. Su ejecución enlaza el nombre de la función en el namespace local actual a un objecto función (un envoltorio alrededor del código ejecutable para la función). Este objeto función contiene una referencia al namespace local global como el namespace global para ser usado cuando la función es llamada.

### La definición de función no ejecuta el cuerpo de la función; esto es ejecutado solamente cuando la función es llamada.

<img src="../imagenes/13.-PycdF.png" width="350" height="150">

### Significado de cada parte del pseudo código fuente anterior:
- NOMBRE, es el nombre de la función.
- LISTA_DE_PARAMETROS, es la lista de parámetros que puede recibir una función.
- DOCSTRING_DE_FUNCION, es la cadena de caracteres usada para documentar la función.
- SENTENCIAS, es el bloque de sentencias en código fuente Python que realizar cierta operación dada.
- return, es la sentencia return en código Python.
- EXPRESION, es la expresión o variable que devuelve la sentencia return.

# Ejemplo: 
<img src="../imagenes/13.-PycdFEj.png" width="500" height="150">

### Salida: 
- ¡Hola Plone!

### La palabra reservada def se usa para definir funciones. Debe seguirle el nombre de la función en el ejemplo anterior hola() y la lista de parámetros formales entre paréntesis. Las sentencias que forman el cuerpo de la función empiezan en la línea siguiente, y deben estar indentado.

### La primer sentencia del cuerpo de la función puede ser opcionalmente una cadena de caracteres literal; esta es la cadena de caracteres de documentación de la función, o docstrings.

# Argumentos y parámetros

### Al definir una función los valores los cuales se reciben se denominan parámetros, pero durante la llamada los valores que se envían se denominan argumentos.

# Por posición

### Cuando envía argumentos a una función, estos se reciben por orden en los parámetros definidos. Se dice por tanto que son argumentos por posición:

### En el ejemplo el argumento 30 es la posición 0 por consiguiente es el parámetro de la función a, seguidamente el argumento 10 es la posición 1 por consiguiente es el parámetro de la función b.

<img src="../imagenes/13.-PycdFP.png" width="500" height="250">

### Salida: 
- 20

# Por nombre

### Sin embargo es posible evadir el orden de los parámetros si indica durante la llamada que valor tiene cada parámetro a partir de su nombre
<img src="../imagenes/13.-PycdFN.png" width="500" height="250">

### Salida: 
- -20

# Funciones anónimas

### Una función anónima, como su nombre indica es una función sin nombre. Es decir, es posible ejecutar una función sin referenciar un nombre, en Python puede ejecutar una función sin definirla con def.

### De hecho son similares pero con una diferencia fundamental, el contenido de una función anónima debe ser una única expresión en lugar de un bloque de acciones.

### Las funciones anónimas se implementan en Python con las funciones o expresiones lambda, esta es unas de las funcionalidades más potentes de Python, pero a la vez es la más confusas para los principiantes.

### Más allá del sentido de función que usted tiene hasta el momento, con su nombre y sus acciones internas, una función en su sentido más trivial significa realizar algo sobre algo. Por tanto se podría decir que, mientras las funciones anónimas lambda sirven para realizar funciones simples, las funciones definidas con def sirven para manejar tareas más extensas.

# Expresión ***lambda***

### Si deconstruye una función sencilla, puede llegar a una función lambda. La siguiente función es para doblar un valor de un número:

<img src="../imagenes/13.-PycdFL1.png" width="500" height="250">

### Salida:
- 4
- <class 'function'>

### Si el código fuente anterior se simplifica se verá, de la siguiente forma:
<img src="../imagenes/13.-PycdFLS1.png" width="500" height="250">

### Salida:
- 4
- <class 'function'>

### Usted puede todavía simplificar más, escribirlo todo en una sola línea, de la siguiente forma:
<img src="../imagenes/13.-PycdFLS2.png" width="500" height="100">

### Salida:
- <function <'lambda'> at 0x1068a8940>

### En este ejemplo tiene una función anónima con una entrada que recibe numero, y una salida que devuelve numero * 2.

### Lo único que necesita hacer para utilizarla es guardarla en una variable y utilizarla tal como haría con una función normal:
<img src="../imagenes/13.-PycdFLSF.png" width="500" height="200">

### Salida:
- 4
- <class 'function'>

# Funciones recursivas

### Las funciones recursivas son funciones que se llaman a sí mismas durante su propia ejecución. Ellas funcionan de forma similar a las iteraciones, pero debe encargarse de planificar el momento en que dejan de llamarse a sí mismas o tendrá una función recursiva infinita.

### Estas funciones se suelen utilizar para dividir una tarea en sub-tareas más simples de forma que sea más fácil abordar el problema y solucionarlo.

# Función recursiva sin retorno

### Ejemplo de una función recursiva sin retorno, este ejemplo es de una cuenta regresiva hasta cero a partir de un número:

<img src="../imagenes/13.-PycdFRSR.png" width="500" height="300">

### Salida:
- 4
- 3
- 2
- 1
- ¡Boooooooom!
- Fin de la función 0
- Fin de la función 1
- Fin de la función 2
- Fin de la función 3
- Fin de la función 4

# Función recursiva con retorno

### Un ejemplo de una función recursiva con retorno, es el ejemplo del calculo del factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número. Es el ejemplo con retorno más utilizado para mostrar la utilidad de este tipo de funciones:

<img src="../imagenes/13.-PycdFRCR.png" width="500" height="300">

### Salida:
- Valor inicial -> 5
- Valor inicial -> 4
- Valor inicial -> 3
- Valor inicial -> 2
- Valor inicial -> 1
- valor final -> 1
- valor final -> 2
- valor final -> 6
- valor final -> 24
- valor final -> 120
- 120

# Generadores

### Un generador es un tipo de función que produce secuencias completos de resultados en lugar de ofrecer un único valor.

### Devuelven los valores con la declaración ***yield***

<img src="../imagenes/13.-PycdFG.png" width="500" height="300">

### Salida:
- uno
- dos
- tres


# Decoradores

### Un decorador es una función Python permite que agregar funcionalidad a otra función, pero sin modificarla. También, esto es llamado meta-programación, por que parte del programa trata de modificar a otro al momento de compilar.

### Los decoradores son una funcionalidad relativamente importante en Python son definidos en el PEP-318. https://peps.python.org/pep-0318/

### Se podría decir que son funciones que modifican la funcionalidad de otras funciones, y ayudan a hacer el código más corto y Pytónico.

### Para llamar un decorador se utiliza el signo de arroba (@).

<img src="../imagenes/13.-PycdFD.png" width="500" height="400">

### Salida:
- Haciendo algo antes de llamar a function()
- Soy la función que necesita ser decorada
- Haciendo algo después de llamar a function()


# Alcance de las funciones
### Las variables que se utilizan deben encontrarse dentro del contexto de ejecución para poder acceder a ellas.

<img src="../imagenes/13.-PycdFAlc.png" width="700" height="300">

### Salida:
- 60
- 30
- 60

#
|  | Descripción |
|-----:|---------------|
| [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion1/index.html#) | ***Documentación oficial*** |
| [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](../Python_NB/Python_NB09.md) | ***Python Básico 09*** |

## Puedes seguir y apoyar mi trabajo haciendo click en "☆ Star" y en el botón de Follow.
## ¡Muchas gracias, bienvenido!!!

## Contacto y apoyo:

<br>[![LinkedIn](https://img.shields.io/badge/Oscar_Florin-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/oscarflorincontreras)
[![X](https://img.shields.io/badge/DevozzCloud-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://twitter.com/DevozzCloud)</br>
[![Just_Eat](https://img.shields.io/badge/🌮_Donaciones_para_tacos-7A1FA2?style=for-the-badge&logo=)](https://paypal.me/OscarFlorin?country.x=MX&locale.x=es_XC)
[![Eats](https://img.shields.io/badge/🐈_Donaciones_para_gatos-black?style=for-the-badge&logo=)](https://paypal.me/OscarFlorin?country.x=MX&locale.x=es_XC)
