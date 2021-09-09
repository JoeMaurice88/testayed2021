"""
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario coincide o no con la variable
 **IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
"""
contraseña= "laboratorio"
try:
    contraseña_usuario= input("Coloque una palabra y ver si coincide con mi contraseña: ")
    contraseña_usuario= contraseña_usuario.lower()

    if contraseña_usuario==contraseña:
        print("La contraseña es la correcta")
    else:
        print("esa no es la contraseña")
except:
    print("ERROR")