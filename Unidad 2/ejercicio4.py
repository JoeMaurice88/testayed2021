"""
El programa debe:
- pedir en orden el Nombre, apellido, edad y numero de calzado
- verificar que cada uno sea el tipo de variable correcto (IMPORTANTE)
- en caso verdadero imprimir de la siguiente manera el resultado:

  ejemplo

  Nombre: Lionel

  Apellido: Messi

  Edad: 34

  Numero de Calzado: 42.5

- en caso contrario imprimir error
"""
try:
  nombre= input("Coloca tu nombre: ")
  apellido= input("Coloca tu apellido: ")
  edad= int(input("Coloca tu edad: "))
  calzado= float(input("Coloca tu calzado: "))
  print(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nCalzado: {calzado}")

except:
  print("¡¡¡ERROR!!!")