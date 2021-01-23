"""
Clase 3 - 28/11/2020
Ejercicio 2 - Manejo de archivos en Python
EducacionIT - Prof. Luciano Pueyo

Martin Nahuel Muñoz Codazzi
30/11/2020

v0.2 2/12/2020

"""
# Haciéndolo así, estoy leyendo dos veces los mismos datos,
# quizás haya otra forma más eficiente. A nivel S.O., no me parece tan mal
# porque liberás el archivo bastante rápido, pero a nivel RAM,
# cargás todo el archivo en memoria... Aunque en R, se hace así XD

import sys

diccionario = {} #Si no lo creo ahora, luego dará error

def lecturaDiccionario(archivo = "archivoC3E2.txt"):
    with open (archivo,"r") as archivo:
        bruto = archivo.read() # leo en bruto todo el archivo
    bruto = bruto.replace(" ","") #elimino espacios por primera vez
    bruto = bruto.split("\n") #Separo por saltos de linea
    bruto.pop() #con esto elimino la basura que deja el comando anterior

    for elemento in bruto:
        #creo una lista de dos elementos por cada elemento
        #también, podría preguntar si me dan una lista vacía
        temporal = elemento.split(":")
        diccionario.update({temporal[0]:temporal[1]})

    return(diccionario)

diccionario = lecturaDiccionario()
#en la llamada a la función, podemos indicarle cualquier archivo
print(diccionario)

sys.exit(0) #Parecee que esto es buena práctica, y lo puedo usar a futuro

# 30/11 No estoy seguro por qué, pero el archivo, debo pasarlo con un
#salto de línea entre cada elementos, quizás se deba a los line endings.
