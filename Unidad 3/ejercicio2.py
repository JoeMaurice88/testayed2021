"""
Agencia de autos:

El programa cuenta con tres marcas de autos y su precio.

El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar
Ford = 10000
Renault = 11000
Chevrolet = 15000
"""
Ford = 10000
Renault = 11000
Chevrolet = 15000
try:
    dinero_usuario= int(input("Ingrese el monto que tiene: "))
    if dinero_usuario>=10000:
        print("Usted puede comprar un fordal, su precio es: ", Ford)
        if dinero_usuario>=11000:
            print("Usted puede comprar un Renault, su precio es: ", Renault)
            if dinero_usuario>15000:
                print("Usted puede comprar un chevroletal, su precio es: ", Chevrolet)
    else:
        print("No le alcanza para comprar")


except:
    print("ERROR")