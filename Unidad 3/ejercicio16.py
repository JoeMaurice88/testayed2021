"""El programa debe:
*    Pedir al usuario un número entero positivo y mostrar por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

Ej: num = 8.

8,7,6,5,4,3,2,1"""


try:
    num_usuario= int(input("ingrese un numero entero: "))   
    for i in range(num_usuario,0,-1):
        print(i)
except:
    print("error")


