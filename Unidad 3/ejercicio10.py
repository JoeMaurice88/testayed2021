flag= True
while flag== True:#DESPUES VEMOS COMO SALIR
  try:
    numero_inicial=int(input("Ingrese un numero incial: "))
    numero_limite=int(input("Ingrese un numero limite: "))
  except:
    print("dije un numero")
  if (numero_inicial<numero_limite):
    while numero_inicial<=numero_limite:
      print(numero_inicial)
      numero_inicial+=1
  else:
    print("el numero incial debe ser menor que el limite")
    flag= False