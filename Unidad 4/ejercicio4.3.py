"""###**Ejercicio 4.2 (Mediciones)**
El programa debe:
*   Contar con 4 funciones (calcular Area (cuadrado), calcular Perimetro(cuadrado),
    calcular Area (circulo), calcular Perimetro(circulo))
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
import math as mt
def perimetro_circulo():
    while True:
        try:
            radio=float(input("Ingrese el radio dl circulo"))
            if radio<=0:
                print("El radio no puede ser menor o igual a 0")
            else:
                break
        except:
            print("error")
    return round(2*mt.pi*radio, 2), radio

perimetro, radio= perimetro_circulo()

print(f"El radio del circulo es: {radio}cm y el perimetro {perimetro}cm")