# Errores y excepciones
<img src="../imagenes/14.-PyE&E.png" width="700" height="400">

### Hay (al menos) dos tipos diferentes de errores: errores de sintaxis y excepciones.

# Errores de sintaxis

### Los errores de sintaxis, también conocidos como errores de interpretación, son quizás el tipo de queja más común que tienes cuando todavía estás aprendiendo Python:

<img src="../imagenes/14.-PycdES.png" width="500" height="140">

### Salida:
-     File "/Users/juanlopez/Desktop/GitHub/Python_Basic/Python_NB/Python_NB09.py", line 2
-     while True print('Hola Mundo')
                 ^^^^^
        - SyntaxError: invalid syntax

### El intérprete repite la línea culpable y muestra una pequeña “flecha” que apunta al primer lugar donde se detectó el error. Este es causado por (o al menos detectado en) el símbolo que precede a la flecha: en el ejemplo, el error se detecta en la sentencia print, ya que faltan dos puntos (':') antes del mismo. Se muestran el nombre del archivo y el número de línea para que sepas dónde mirar en caso de que la entrada venga de un programa.

# Excepciones

### Incluso si la sentencia o expresión es sintácticamente correcta, puede generar un error cuando se intenta ejecutarla. Los errores detectados durante la ejecución se llaman excepciones, y no son incondicionalmente fatales. Sin embargo, la mayoría de las excepciones no son manejadas por los programas, y resultan en mensajes de error como los mostrados aquí:

<img src="../imagenes/14.-PycdEE.png" width="400" height="150">

### Salida:
-     10 * (1/0)
-     ZeroDivisionError: division by zero

-     4 + leonardo * 3
-     NameError: name 'leonardo' is not defined

-     "2" + 2
-     TypeError: can only concatenate str (not "int") to str

### La última línea de los mensajes de error indica qué sucedió. Las excepciones vienen de distintos tipos, y el tipo se imprime como parte del mensaje: los tipos en el ejemplo son: ZeroDivisionError, NameError y TypeError.

### La cadena mostrada como tipo de la excepción es el nombre de la excepción predefinida que ocurrió. Esto es verdad para todas las excepciones predefinidas del intérprete, pero no necesita ser verdad para excepciones definidas por el usuario (aunque es una convención útil). Los nombres de las excepciones estándar son identificadores incorporados al intérprete (no son palabras clave reservadas).

### El resto de la línea provee un detalle basado en el tipo de la excepción y qué la causó.

### La parte anterior del mensaje de error muestra el contexto donde la excepción sucedió, en la forma de un trazado del error listando líneas fuente; sin embargo, no mostrará líneas leídas desde la entrada estándar.

### Excepciones integradas, es una lista las excepciones predefinidas y sus significados.

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
