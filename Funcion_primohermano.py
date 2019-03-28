print("Funcion que me indique si un numero es primohermano o no")

n=int(input("Digita un numero, Por favor: "))

def hermano(n):
	if n%6==0:
		print("El numero " + str(n) + " no es primohermano")
	else:
		cont=0
		b=n+1
		for i in range(1,b+1):
			if b%i==0:
				cont+=1
		if cont>2:
			print("El numero " + str(n) + " no es primohermano")
		else:
			print("El numero " + str(n) + " es primohermano")

hermano(n)

print("Final del programa")

