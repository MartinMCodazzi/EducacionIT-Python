"""
Funcion Factorial - Martin Nahuel Muñoz Codazzi

22/11/2020
"""

def factor(numero):
    if numero > 1 :
        for i in range(numero-1, 0, -1):
             numero*= i
    return(numero)


x = int(input("Ingrese el número que quiera saber su factor: "))

for i in range (x):
    print("El factorial de " + str(i+1) + " es : " + str(factor(i+1)))
