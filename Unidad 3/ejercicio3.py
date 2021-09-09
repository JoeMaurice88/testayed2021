"""
El programa debe:

Pedir al usuario 3 notas de 3 parciales diferentes
verificar que los ingresados sean correctos
En caso correcto imprimir el promedio
En caso contrario imprimir un error
"""
try:
    nota_1= float(input("Ingrese su primer nota: "))
    nota_2= float(input("Ingrese su segunda nota: "))
    nota_3= float(input("Ingrese su tercera nota: "))
    promedio=(nota_1+nota_2+nota_3)/3
    
    
except:
    print("ERROR")

if promedio>=5 and promedio<7:
    print(f"Usted esta en estado regular con el promedio de {promedio}")
elif promedio>=7 and promedio<=10:
    print(f"Usted esta en estado promocionado con el promedio de {promedio}")
else:
    print(f"Usted esta en estado libre con el promedio de {promedio}")