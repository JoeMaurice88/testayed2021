"""
###**Ejercicio 4.3 (Palabras)**
El programa debe:
*   Contar con 3 funciones:
    1. Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o 
    frase (letra y frace deben ambos ser parametros)
    2. Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.
    IMPORANTE: deben ser palabras y no frases (verificar)
    3. Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y 
    quitar todas las vocales
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def comparador(palabra1, palabra2):
    contador1=0
    contador2=0
    
    while True:
        for i in palabra1:
            if i != " ":
                contador1+=1
            else:
                print("no es una palabra es una frase")
        break
    while True:
        for i in palabra2:
            if i != " ":
                contador2+=1
            else:
                print("no es una palabra es una frase")        
        break
    if contador1>contador2:
        print(f"{palabra1} es mayor")
    elif contador1<contador2:
        print(f"{palabra2} es mayor")
    else:
        print(f"las 2 palabras tienen la misma cantidad de letras, palabra 1 {palabra1} y palabra 2 {palabra2}")
comparador("Joser","Amor")
