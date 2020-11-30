"""
Clase 3 - 28/11/2020
Ejercicio 1 - Manejo de archivos en Python
EducacionIT - Prof. Luciano Pueyo

Martin Nahuel Muñoz Codazzi
29/11/2020

"""

def escrituraArchivo(coleccion):
    with open ("archivoPrueba.txt", "w") as archivo:
        for elemento in coleccion :
            archivo.write(str(coleccion[elemento -1])")  
            #Hay que hacer casting a String para escribir. El -1 porque me daba error de "out of range"
            # No puedo hacer un , + \n en la linea anterior, por eso va la siguiente
            
            archivo.write("\n")
            #Sin esta linea, me escribe uno al lado del otro, lástima que writeln no funcione

lista = list(range(1,101))
escrituraArchivo(lista)

