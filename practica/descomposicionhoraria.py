while True:
    tiempo = int(input("Número positivo de segundos: "))
    if tiempo >= 0:
        print("Horas: " + str(tiempo // 3600))
        minutos = int((tiempo % 3600) / 60)
        segundos = int((tiempo % 3600) % 60)
        print("Minutos: " + str(minutos))
        print("Segundos: " + str(segundos))

