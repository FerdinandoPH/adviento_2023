with open("dia1p1.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]
  suma=0
  for linea in lineas:
    primero=None
    ultimo=None
    for i,caracter in enumerate(linea):
      if caracter.isdigit():
        if primero is None:
          primero=int(caracter)
        else:
          ultimo=int(caracter)
    if ultimo is None:
      ultimo=primero
    print(primero,"+",ultimo,"=",primero*10+ultimo)
    suma+=primero*10+ultimo
  print(suma)