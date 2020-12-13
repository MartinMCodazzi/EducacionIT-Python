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

Mi_perro = Dog("Totito", 6)

Mi_perro.sit()
Mi_perro.bark()

separador()

##  EJERCICIO 9-1  ##

class Restaurante:
    def __init__(self, nombre, tipo_cocina):
        self.nombre = nombre.title()
        self.tipo_cocina = tipo_cocina
        self.numero_clientes = 0

    def describe(self):
        print("Restaurante : " + self.nombre.title() + \
         "\nTipo de cocina : " + self.tipo_cocina.title())
        separador()

    def abierto(self):
        print(self.nombre.title() + " está ahora abierto.")

    def set_numero_clientes(self, numero):
        self.numero_clientes = numero

    def inc_numero_clientes(self, arg = 1):
        self.numero_clientes += arg


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

    def __init__(self, nombre, apellido, usuario, password):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario.lower()
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        separador()
        print("El usuario se llama : " + self.nombre.title() + " " + self.apellido.upper() \
              + "\nSu nombre de usuario es : " + self.usuario   \
              + "\nSu contraseña es : " + self.password)
        separador()

    def saludo(self):
        print("bienvenido al sistema, " + self.nombre.title() + " " + self.apellido.upper())
        separador()

    def inc_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

usu1 = Usuario("Martin" , "Codazzi", "root", "root")
usu2 = Usuario("pedro" , "perez", "pperez", "1234")
usu3 = Usuario("pablo" , "gonzalez", "pgonzalez", "1234")

usu1.describe_user()
usu2.describe_user()
usu3.describe_user()

usu1.saludo()
usu2.saludo()
usu3.saludo()


##  EJERCICIO 9-4 ##

Resto1.set_numero_clientes(20)
print(Resto1.numero_clientes)
Resto1.inc_numero_clientes()
Resto1.inc_numero_clientes(2)
print(Resto1.numero_clientes)

## EJERCICIO 9-5 ##

separador()
usu1.inc_login_attempts()
usu1.inc_login_attempts()
print(usu1.login_attempts)
usu1.reset_login_attempts()
print(usu1.login_attempts)
separador()

## EJERCICIO 9-6 ##

class Heladeria(Restaurante):
    def __init__(self, nombre, tipo_cocina, *sabores):
        super().__init__(nombre, tipo_cocina)
        self.sabores = [sabor.title() for sabor in sabores] # JA!

helados1 = Heladeria("piu", "heladeria", "dulce de leche", "chocolate", "frutilla", "vainilla", "durazno", "menta granizada")
print(helados1.sabores)
print(helados1.nombre)

## EJERCICIO 9-7 ##

separador()

class Privilegios:
    def __init__(self, *args):
        self.privilegios = (privilegio.title() for privilegio in args)

    def mostrar_privilegios(self):
        [print(privilegio) for privilegio in self.privilegios]

class Admin(Usuario):
    def __init__(self, nombre, apellido, usuario, password, *args):
        super().__init__(nombre, apellido, usuario, password)
        self.privil = Privilegios(*args)

root = Admin("root", "root", "root", "toor", "can add post", "can delete post", "can ban user")
root.describe_user()
#root.mostrar_privilegios()

## EJERCICIO 9-8 ##

root.privil.mostrar_privilegios()
# jajaja, que matete!
