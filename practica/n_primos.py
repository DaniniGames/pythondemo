def es_primo(x):
	if x % 2 == 0: 
		print("Es primo")
	else:
		print("Es impar")

es_primo(325)

def primos_hasta(x):
	for i in range(x):
		if i % 2 == 0:
			print(i)

primos_hasta(15)
