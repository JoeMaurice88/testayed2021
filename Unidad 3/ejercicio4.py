"""
El programa debe :
*    Pedir al usuario un string
*    Determinar si una cadena esta en minusculas o mayusculas
"""

dato_1= input("Ingrese algun dato: ")

if dato_1.islower():
    print("El dato que escribiste esta en minuscula")
elif dato_1.isupper():
    print("El dato que escribiste esta en mayuscula")
else:
    print("El dato ingresado posee mayusculas y minusculas")