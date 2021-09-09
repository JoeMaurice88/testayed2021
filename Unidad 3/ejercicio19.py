"""
El programa debe:
*   Pedir al usuario una palabra
*   Verificar que sea una palabra y no un numero
*   Mostrar por pantalla las letras una a una
*   No producir errores
"""
while True:
    palabra= input("Ingrese una palabra: ")
    if palabra.isalpha():
        for i in palabra:
            print(i)
        break
    else:
        print("error")
