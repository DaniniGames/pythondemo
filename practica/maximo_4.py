def maximo(x, y):
	if x > y:
		return x
	else:
		return y

def maximo_4(x, y, z, n):
	a = maximo(x, y)
	b = maximo(z, n)
	print(maximo (a, b))


maximo_4(5423, 8211187737, 9211221, 459999999991221)
