"""
Clase 3 - 28/11/2020
Ejercicio 2 - Manejo de archivos en Python
EducacionIT - Prof. Luciano Pueyo

Martin Nahuel Muñoz Codazzi
30/11/2020

"""
diccionario = {}

def lecturaDiccionario():
    with open ("archivoC3E2.txt","r") as archivo:
        for elemento in archivo:
            txt = archivo.readline()
            txt = txt.split()
            diccionario.update({txt[0]:txt[1]})
    return(diccionario)

diccionario = lecturaDiccionario()
print(diccionario)


# 30/11 No estoy seguro por qué, pero el archivo, debo pasarlo con un  
#salto de línea entre los elementos.
