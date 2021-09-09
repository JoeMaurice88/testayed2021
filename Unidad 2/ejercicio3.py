"""
El programa debe:
- pedir dos datos por consola
- verificar que los dos datos sean numeros enteros
- en caso verdadero imprimir la suma de ambos
- en caso contrario imprimir error
"""

try:
    dato1= int(input("Ingrese un dato: "))
    dato2= int(input("ingrese otro dato: "))
    print(f"la suma de los 2 numeros es: {dato1+dato2}")
except:
    print("ERROR!!")