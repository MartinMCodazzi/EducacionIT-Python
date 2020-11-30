def fibo(iteraciones):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,iteraciones):
	    c = a + b
	    print(c)
	    a = b
	    b = c	    
 
 
 
veces = int(input("Ingrese la cantidad de términos a mostrar: "))

if veces > 1:
    fibo(veces)
else:
    print("Incorrecto")
    
