apetece = input("Quieres un helado? ").lower()
if apetece == "si":
	apetece = True

eco = input("Tienes dinero? ").lower()
if eco == "si":
	eco = True

tienda = input("La tienda está abierta? ").lower()
if tienda == "si":
	tienda = True

if apetece == True and eco == True and tienda == True:
	print("Disfrútalo.")
else:
	print("No puedes disfrutarlo.")