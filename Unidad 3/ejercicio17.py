"""El programa debe:
*     Preguntar al usuario una cantidad a invertir
*     Preguntar al usuario el interés anual y el número de años
*     Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión"""
inversion_acumulada=0
ganancia_total= 0
ganancia= 0
inversion= float(input("Ingrese el monto que desea para invertir: "))
interes= float(input("porcentaje deseadopor año: "))
años= int(input("cantidad de años que quiere realizar el plazo fijo: "))

for i in range(1,años +1):
    inversion= inversion*(interes/100)+inversion
    
    ganancia_total+=inversion
    print(f"ganancia anual es de {inversion}")
print("ganancia total", ganancia_total)
