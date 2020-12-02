"""
Clase 3 - 28/11/2020
Alumni Ejercicio 1 - Manejo de excepciones en Python
EducacionIT - Prof. Luciano Pueyo

Martin Nahuel Muñoz Codazzi
01/12/2020

"""
import sys

paises = {
            "ar": "Argentina",
            "es": "España",
            "us": "Estados Unidos",
            "fr": "Francia"
}

while True:

    entradaPais = input("Ingrese el código de pais, o salir, para salir: ")
    if entradaPais == "salir" or entradaPais == "Salir":
        print("Hasta Luego")
        break
    else:
        try:
            print(paises[entradaPais])

        except KeyError:
            print("Pais no encontrado.")

sys.exit()
