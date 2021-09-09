duracion_total=0
cant_tramos=0
cant_duracion=0
    
try:
    cant_tramos= int(input("Ingrese la cantidad de tramos que va a realizar: "))
    cant_duracion= int(input("Cuantos minutos por cada tramo: "))
    for i in range(0,cant_tramos):
        duracion_total += cant_duracion

    if duracion_total>=60:
        print("---"*15)
        print(f"en {cant_tramos} tramos, de {cant_duracion} minutos, su viaje duro: {duracion_total//60} horas y {duracion_total%60} minutos")
    else:    
        print(f"en {cant_tramos} tramos, de {cant_duracion} minutos, su viaje duro: {duracion_total}")
    print("Fin del programa")
except:
    print("ERROR")