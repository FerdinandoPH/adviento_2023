with open("dia9.txt","r") as f:
  lineas=[i.rstrip() for i in f.readlines()]
  suma=0
  for linea in lineas:
    diferencias=[]
    lista_valores=[int(i) for i in linea.split(" ")]
    diferencias.append(lista_valores[0])
    while lista_valores!=[0]*len(lista_valores):
      valores_temporales=[]
      for i in range(1,len(lista_valores),1):
        valores_temporales.append(lista_valores[i]-lista_valores[i-1])
      lista_valores=valores_temporales.copy()
      diferencias.append(lista_valores[0])
    suma_de_linea=0
    for i,numero in enumerate(diferencias):
      suma_de_linea+=numero*((-1)**i)
    suma+=suma_de_linea
  print("Resultado:",suma)