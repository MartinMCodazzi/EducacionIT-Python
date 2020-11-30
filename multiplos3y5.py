x = int(input("Ingrese el valor máxinmo: "))

lista = []

for i in range(1, x+1):
    if i % 5 == 0:
        if i % 3 == 0:
            lista.append(i)
print(lista)
