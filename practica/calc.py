import math

print("****CALCULADORA****")

while True:
    o = input('"s" para sumar, "r" para restar, "d" para dividir, m "para multiplicar o "rc" para raiz cuadrada: ')

    if o == "s":
        x = input("1r sumando: ")
        y = input("2do sumando: ")
        z = input("3r sumando: ")
        print("Total: " + str(float(x) + float(y) + float(z)))

    elif o == "r":
        x = input("Minuendo: ")
        y = input("Substraendo: ")
        print("Diferencia: " + str(float(x) - float(y)))

    elif o == "d":
        x = input("Dividendo: ")
        y = input("Divisor: ")
        print("Cociente: " + str(float(x) / float(y)) + " y resto: " + str(float(x) % float(y)))

    elif o == "m":
        x = input("1r factor: ")
        y = input("2do factor: ")
        print("Producto: " + str(float(x) * float(y)))

    elif o == "rc":
        x = input("Radicando: ")
        x = float(x)
        print("Raíz: " + str(math.sqrt(x)))
