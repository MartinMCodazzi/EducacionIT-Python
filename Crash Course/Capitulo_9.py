# Capítulo 9, Clases

separador = lambda: print ("*" * 25)

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " Se esta sentando")

    def bark(self):
        print(self.name + " Está ladrando" )

Mi_perro = Dog("totito", 6)

Mi_perro.sit()
Mi_perro.bark()

separador()

##  EJERCICIO 9-1  ##

class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina

    def describe(self):
        print("Restaurante : " + self.nombre.title() + \
         "\nTipo de cocina : " + self.tipo_cocina.title())
        separador()

    def abierto(self):
        print(self.nombre.title() + " está ahora abierto.")


Resto1 = Restaurante("macdonalds", "rapida")
print (Resto1.nombre)
print (Resto1.tipo_cocina)

separador()

Resto1.describe()
Resto1.abierto()

separador()
##  EJERCICIO 9-2 ##
separador()

Resto2 = Restaurante("mostaza","rapida")
Resto3 = Restaurante("pizzaYA","pizzería")
Resto4 = Restaurante("kansas", "parrilla")

Resto2.describe()
Resto3.describe()
Resto4.describe()

separador()
##  EJERCICIO 9-3 ##
separador()

class Usuario:
    """Ejercicio 9-3"""

    def __init__(self, nombre, apellido, usuario, password, privilegios=None):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario.lower()
        self.password = password
        self.privilegios = privilegios

    def describe_user(self):
        print("El usuario se llama " + self.nombre.title() + " " + self.apellido.upper() \
              + "\nSu nombre de usuario es : " + self.usuario \
              + "\nSu ncontraseña es : " + self.password \



        )
