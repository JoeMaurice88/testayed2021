"""
El programa debe:

- pedir el ingreso de un número positivos al usuario y almacenar la respuesta en la variable numero.
- Verificar que se trate de un numero entero y sino mostrar un error
- Comprobar si el número es negativo. Si lo es, el programa debe avisa que no era eso lo que se había pedido. (si no hay error)
- Finalmente imprimir siempre el valor introducido por el usuario.(si no hay error)
"""
try:

    num_entero= int(input("Ingrese un numero entero: "))
    if num_entero < 0:
        print("el numero es menor a 0")
    print(f"el valor ingresado es: {num_entero}")
except:
    print("ERROR")
