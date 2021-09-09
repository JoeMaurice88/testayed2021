"""El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""

while True:
    palabra= input("Ingrese una palabra: ")
    
    
    
    if palabra== "salir":
        break
    elif palabra!= "salir":
        if palabra == "hola" or palabra== "chau":
            continue
        else:
            print(palabra)

"""CORREJIR!!!!!!!!!"""
            
    
    