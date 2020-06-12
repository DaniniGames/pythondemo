lista=[]
añadir = input("Añadir productos: ") 

while añadir != "fin":
	lista.append(añadir)
	añadir = input("Añadir productos. 'fin' para ver la lista: ") 

print (lista)
