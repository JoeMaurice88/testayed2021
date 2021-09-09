"""El programa debe:
*  pedir al usuario 5 datos numericos
*  verificar que sean enteros y sino pedir nuevamente los 5
*  cuando se tenga los 5 datos el programa debe devolver el promedio
*  no deben aparecer errores."""
i=1
acumulador= 0

try:
    while i <= 5:
        dato_numerico= int(input("Ingrese un dato numerico: "))
        i+=1
        acumulador+= dato_numerico
        print(f"El promdio de las notas es de: {acumulador/5}")    
except:
    print("error")    