###**Ejercicio 4.1 (Calculadora)**
"""El programa debe:
*   Contar con 4 funciones (suma, resta, división y multiplicación)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los dos numero para operar y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def sumador(a,b):
    suma = float(a)+float(b)
    return suma

def restador(a,b):
    resta = float(a)-float(b)
    return resta

def divisor(a,b):
    while True:
        if b!=0:
            division = float(a)/float(b)
            break
        else:
            print("No es posible dividir por 0")
            a,b = pedir_numeros()     
    return round(division, 4)

def multiplicador(a,b):
    multiplicacion = float(a)*float(b)
    return round(multiplicacion, 4)

def pedir_numeros():
    while True:
        try:
            num1 = float(input("1° Argumento: "))
            num2 = float(input("2° Argumento: "))
            break
        except:
            print("argumentos incorrectos")

    return num1,num2


while True:
    condicion=input(
"""Por favor ingrese una opcion
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. Salir
Numero : """)
    if (condicion=="1"):
        a,b = pedir_numeros()
        print (f"La suma de {a} + {round(b,4)} = {sumador(a,b)}")
    elif (condicion=="2"):
        a,b = pedir_numeros()
        print (f"La resta de {a} - {b} = {restador(a,b)}")
    elif (condicion=="3"):
        a,b = pedir_numeros()
        print (f"La multiplicacion de {a} * {b} = {multiplicador(a,b)}")
    elif (condicion=="4"):
        a,b = pedir_numeros()
        print (f"La division de {a} / {b} = {divisor(a,b)}")
    elif (condicion=="5"):
        break
    else:
        print("ninguna opcion correcta")
