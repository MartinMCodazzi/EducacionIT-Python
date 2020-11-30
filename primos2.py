"""
Calculador de rango de números primos

Martin Nahuel Muñoz Codazzi

22/11/2020

"""

def primo(numero):
    for i in range (2,numero):
        if numero % i == 0:
            return(None)
            break
            # ~ return (str(numero) + " No es primo")
            
    else:
        return (str(numero) + " es primo")


x = int(input("Ingrese el número máximo que quiere saber si es primo: "))
for i in range(1,x+1):
    resultado = primo(i)
    if resultado:
        print(resultado)
