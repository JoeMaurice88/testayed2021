"""*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""
def conv_grados():
    while True:
        try:
            celcius= float(input("Ingrese una temperatura en grados celcius: "))
            return celcius*9/5+32, celcius
        except:
            print("dato erroneo")
            

def conv_cm3():
    while True:
        try:
            cm3= float(input("Ingrese cantidad en cm3: "))
            if cm3<0:
                print("Dato mal ingresado o menos a 0")
            else:
                return cm3/1000, cm3
        except:
            print("Dato mal ingresado")
    
        
			
	
def conv_litros():
    while True:
        try:
            litro= float(input("Ingrese cantidad en litros: "))
            if litro<0:
                print("Dato mal ingresado o menos a 0")
            else:
                return litro*1000, litro
        except:
            print("Dato mal ingresado")

def conv_pesos():
    while True:
        try:
            pesos= float(input("Ingrese cantidad en pesos:$ "))
            if pesos<0:
                print("Dato mal ingresado o menos a 0")
            else:
                return round(pesos/180, 2), pesos
        except:
            print("Dato mal ingresado")



while True:
    try:
        opcion= int(input("""
    Menu de opciones
    1. Convertidor de grados Celcius a Fahrenheit
    2. Conversor de cm3 a litros
    3. Conversor de litros a cm3
    4. Conversor de peso a dolar
    5. Salir

    Ingrese la opcion: """))
    

        if opcion== 1:
            fahrenheist, celcius= conv_grados()
            print(f"grados celcius {celcius}° y pasados a fahrenheist es: {fahrenheist}°")
        if opcion== 2:
            litro, cm3= conv_cm3()
            print(f"{cm3} cm3 pasados a litros es: {litro} litros")
        elif opcion== 3:
            cm3, litros= conv_litros()
            print(f"{litros} litros pasados a cm3 es: {cm3} litros")
        elif opcion== 4:
            dolares, pesos= conv_pesos()
            print(f"${pesos}pasados a dolares es: U${dolares}")
        elif opcion== 5:
            break
    except:
        print("Dato erroneo")