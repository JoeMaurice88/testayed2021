
lista=[]


try:	
	cant_persona= int(input("Ingrese la cantidad de personas: "))
	for i in range(1, cant_persona+1):
		while True:
			edad = int(input(f"Que edad tiene la {i}° persona: "))
			if edad>0:
				lista.append(edad)
				break
			else:
				print("la edad es erronea")
	print(f"De todas estas edades {lista}\nLa edad mas grande es: {max(lista)}")
except:
	print("Dato erroneo")