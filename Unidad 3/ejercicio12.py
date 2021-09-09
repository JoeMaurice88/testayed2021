"""El programa debe:

pedir al usuario una palabra
pedir un numero al usuario
mostrar la palabra por pantalla la cantidad de veces que diga el numero
no debe generar errores"""
i= 1

palabra= input("Ingrese una palabra: ")

if palabra.isalpha():
    while True:
        numero= input("Ingrese un numero: ")
        if numero.isdigit():
            numero= int(numero)
            break
        else:
            print("no es un numero entero")
else:
    print("no es un dato string")
while i <= numero:
    print(palabra)
    i+=1
