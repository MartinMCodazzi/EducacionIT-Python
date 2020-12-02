"""
Clase 3 - 28/11/2020
Alumni Ejercicio 2 - Manejo de excepciones en Python
EducacionIT - Prof. Luciano Pueyo

Martin Nahuel Muñoz Codazzi
01/12/2020

"""
import sys
import os          # Esto sirve para usar el os.system("clear")

def separador(cha = "*", veces = 30):
    print(str(cha * veces))

while True:
# De este while solo se sale teniendo dos numeros enteros
# Habría usado isinstance(), pero no se puede usar if
    try:
        numero1 = int(input("Ingrese un número : "))
        numero2 = int(input("Ingrese otro número : "))

    except (TypeError, ValueError):
        print("Por favor ingrese un número entero")
        #No se por que tuve que poner ambas excepciones
    else:
        #os.system("clear") # En Windows sería os.system("cls")
        break

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

try:
    division = numero1 / numero2
    # Me gusta hacerlo así, bien especifico para cada punto de fallo

except ZeroDivisionError:
    division = str("No se puede dividir por cero")
    # Uso la propiedad de las variables que no tienen tipo, para pasar string

separador()
print ("El resultado de la suma es: ", str(suma))
print ("El resultado de la resta es: ", str(resta))
print ("El resultado de la multiplicacion es: ", str(multiplicacion))
print ("El resultado de la division es: ", str(division))

sys.exit()  # buena práctica?
