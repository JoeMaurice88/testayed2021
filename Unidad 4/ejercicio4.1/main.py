#PARA IMPORTAR DESDE OTRA CARPETA SE HACE DE ESTA FORMA
#from unidad_4(ejemplo) import funciones as fn

import funciones as fn #fn es la abreviatura para pedir (fn.)

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
        a,b = fn.pedir_numeros()
        print (f"La suma de {a} + {round(b,4)} = {fn.sumador(a,b)}")
    elif (condicion=="2"):
        a,b = fn.pedir_numeros()
        print (f"La resta de {a} - {b} = {fn.restador(a,b)}")
    elif (condicion=="3"):
        a,b = fn.pedir_numeros()
        print (f"La multiplicacion de {a} * {b} = {fn.multiplicador(a,b)}")
    elif (condicion=="4"):
        a,b = fn.pedir_numeros()
        print (f"La division de {a} / {b} = {fn.divisor(a,b)}")
    elif (condicion=="5"):
        break
    else:
        print("ninguna opcion correcta")
