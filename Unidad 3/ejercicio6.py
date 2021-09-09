"""
Determinar si una persona tiene fiebre. (fiebre : 37.5 grados) o tiene menos de 30° y sino esta sano
"""
temperatura= float(input("Ingrese su temperatura: "))
if temperatura>= 37.5:
    print("tiene fiebre")
elif temperatura<= 30:
    print("tiene baja temperatura")
else:
    print("Estas sano")
    