print ("*****CÁLCULO IMC*****")

peso_belico = float(input ("Introduce tu peso (KG): "))
altura_belica = float(input ("Introduce tu altura (M): "))

imc = peso_belico / altura_belica ** 2
imc_belico = round(imc, 2)

clasificacion_belica = ""
if imc < 18.5:
	clasificacion_belica = "peso insuficiente"
elif imc > 18.5 and imc < 24.9:
	clasificacion_belica = "normopeso"
elif imc > 24.9 and imc < 26.9:
	clasificacion_belica = "sobrepeso grado I"
elif imc > 26.9 and imc < 29.9:
	clasificacion_belica = "sobrepeso grado II"
elif imc > 29.9 and imc < 34.9: 
	clasificacion_belica = "obesidad tipo I"
elif imc > 34.9 and imc < 39.9:
	clasificacion_belica = "obesidad tipo II"
elif imc > 39.9 and imc < 49.9:
	clasificacion_belica = "obesidad tipo III (mórbida)"
elif imc > 49.9:
	clasificacion_belica = "obesidad tipo IV (extrema)"

print ("Tu IMC es de " + str(imc_belico) + ", así que tienes " + clasificacion_belica + ".")
