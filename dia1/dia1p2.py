with open("dia1p1.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]
  suma=0
  nums={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
  for linea in lineas:
    primero=None
    ultimo=None
    for i,caracter in enumerate(linea):
      if caracter.isdigit():
        if primero is None:
          primero=int(caracter)
        else:
          ultimo=int(caracter)
      else:
        for num in nums:
          if linea[i:].startswith(num):
            if primero is None:
              primero=nums[num]
            else:
              ultimo=nums[num]
    if ultimo is None:
      ultimo=primero
    print(primero,"+",ultimo,"=",primero*10+ultimo)
    suma+=primero*10+ultimo
  print(suma)