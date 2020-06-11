x = int(input("Cuántos números? "))

n1, n2 = 0, 1

for i in range(x):
	nth = n1 + n2
	n1 = n2
	n2 = nth
	print(n1)
