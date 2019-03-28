print("Funcion que me imprima si un numero es primo o no")

n=int(input("Digita un numero, Por favor: "))

def primo():
	cont=0
	for i in range(1,n+1):
		if n%i==0:
			cont+=1
	if cont>2:
		print("El numero " + str(n) + " no es un numero primo")
	else:
		print("El numero " + str(n) + " es un numero primo")

primo()

print("Final del programa")


			