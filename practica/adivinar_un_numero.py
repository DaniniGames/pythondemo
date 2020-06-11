import random

adivinanza = random.randrange(1,10)

entrada = int(input("Adivina el número entre 1 y 10: "))

while entrada != adivinanza:
	if entrada > adivinanza:
		print("El número a adivinar es menor.")
	else:
		print("El número a adivinar es mayor.")
	entrada = int(input("Adivina el número entre 1 y 10: "))

print("Bien.")
