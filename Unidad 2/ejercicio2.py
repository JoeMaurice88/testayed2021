"""
El programa debe:

pedir por teclado el dinero actual de una persona
pedir por teclado el precio del insumo que quiere comprar en USD
convertir ese dinero a dolares( 1USD -> 170$)
devoler por pantalla True en caso que pueda comprar, False en caso que no
No deben aparecer errores
"""
try:
    dinero_usuario= float(input("cuanto dinero tienes: "))
    precio_en_dolar= float(input("ingrese el precio del insumo que quiere comprar: "))
    dinero_actual_UDS = dinero_usuario/170
    print(dinero_actual_UDS>=precio_en_dolar)
except:
    print("error de escritura")