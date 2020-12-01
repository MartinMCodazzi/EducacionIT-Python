"""
Clase 3 - 28/11/2020
Ejercicio 2 - Manejo de archivos en Python
EducacionIT - Prof. Luciano Pueyo

Martin Nahuel Muñoz Codazzi
30/11/2020

"""
import sys

diccionario = {} #Si no lo creo ahora, luego dará error

def lecturaDiccionario(archivo = "archivoC3E2.txt"):
    with open (archivo,"r") as archivo:
        for elemento in archivo:            #Para leer hasta EOF
            txt = archivo.readline()        #leo una línea
            txt = txt.replace(":","")       #cambio el ":" por Vacío
            txt = txt.split()               #Divido ambos términos, generando
                                            #Una lista de dos elementos
            diccionario.update({txt[0]:txt[1]})
    return(diccionario)

diccionario = lecturaDiccionario()
#en la llamada a la función, podemos indicarle cualquier archivo
print(diccionario)

sys.exit(0) #Parecee que esto es buena práctica, y lo puedo usar a futuro

# 30/11 No estoy seguro por qué, pero el archivo, debo pasarlo con un
#salto de línea entre cada elementos, quizás se deba a los line endings.
