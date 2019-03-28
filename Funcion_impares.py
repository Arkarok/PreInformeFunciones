print("Funcion que imprima n cantidad de numeros impares")

n=int(input("Digita un numero, Por favor: "))

def impar():
	for i in range(1,n+1):
		if i%2!=0:
			print(i)
impar()

print("Final del programa")

			