# Alcance ejemplo.
edad = 60 # Esta es una variable GLOBAL
def edad():
    edad = 30 # Esta es una variable LOCAL
    if edad > 50 :
        print(edad)

print(edad)
edad()
print(edad)