print("Funcion que imprima un numero a elevado en b")

def potencia():
	for i in range(0,2):
		i+=1
		a=float(input("Digita un numero, Por favor: "))
		b=float(input("Digita un numero, Por favor: "))
		if i==1:
			x1=a**b
			print(x1)
		else:
			x2=a**b
			print(x2)
	if x1>x2:
		print(str(x1) + " es mayor que " + str(x2))
	elif x1==x2:
		print("Son iguales")
	else:
		print(str(x2) + " es mayor que " + str(x1))

potencia()

print("Final del programa")

			