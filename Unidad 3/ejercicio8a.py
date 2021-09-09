menu="""
Munú de colores
1- Rojo
2 - Azul
3 - Verde
""" # creamos una variable con un strings en varias lineas para ser mas legible el menu
try:# colocamos un try except por si llega el usuario colocar algun dato erroneo y el programa deje de funcionar
    print(menu)
    opcion= int(input("Elija un color tipeando el número correspondiente: "))#Pedimos datos al usuario dependiendo del menu

    # creamos una sentencia if elif y else para poder ser dividido el menu con sus diferentes opciones
    # dentro de estas, se realizan otras sentencias pidiendo mas datos al usuario
    if opcion== 1:
        print("Usted a elejido el color Rojo")
        segunda_opcion= int(input("Elija otro color\n2 - Azul\n3 - Verde\nElija el color tipeando el número correspondiente: "))
        if segunda_opcion== 2:
            print("Usted a elejido el color Azul")
            print("La combinación de color es: Morado")
        elif segunda_opcion== 3:
            print("Usted a elejido el color Verde")
            print("La combinación de color es: Marron")
        else:
            print("La opción colocada no es correcta")
    elif opcion== 2:
        print("Usted a elejido el color Azul")
        segunda_opcion= int(input("Elija otro color\n1 - Rojo\n3 - Verde\nElija el color tipeando el número correspondiente: "))
        if segunda_opcion== 1:
            print("Usted a elejido el color Rojo")
            print("La combinación de color es: Morado")
        elif segunda_opcion== 3:
            print("Usted a elejido el color Verde")
            print("La combinación de color es: Cyan")
        else:
            print("La opción colocada no es correcta")
    elif opcion== 3:
        print("Usted a elejido el color Verde")
        segunda_opcion= int(input("Elija otro color\n1 - Rojo\n2 - Azul\nElija el color tipeando el número correspondiente: "))
        if segunda_opcion== 1:
            print("Usted a elejido el color Rojo")
            print("La combinación de color es: Amarillo")
        elif segunda_opcion== 2:
            print("Usted a elejido el color Azul")
            print("La combinación de color es: Cyan")
        else:
            print("La opción colocada no es correcta")
    else:
        print("La opción colocada no es correcta")
except:
    print("Dato ingresado erroneo")