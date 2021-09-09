"""Ejercicio (Ahora con flag)**
El programa debe:
*  pedir un dato al usuario
*  solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto",
 en caso contrario debe seguir pidiendo el dato
*  no deben aparecer errores."""

flag= True    
while flag:
    dato_1= input("Ingrese un dato: ")
    dato_1= dato_1.lower()    
    if dato_1 == "python":
        print("Correcto")
        flag= False
    else:
        print("Es incorrecto")