import random

adivinanza = random.randrange(1,10)

entrada = int(input("Adivina el número entre 1 y 10: "))

if entrada == adivinanza:
    print("Bien.")
elif entrada > adivinanza:
    print("Es menor.")
else:
    print("Es mayor.")