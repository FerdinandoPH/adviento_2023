with open("dia9.txt","r") as f:
  lineas=[i.rstrip() for i in f.readlines()]
  suma=0
  for linea in lineas:
    tablas=[]
    diferencias=[]
    lista_valores=[int(i) for i in linea.split(" ")]
    tablas.append(lista_valores)
    diferencias.append(lista_valores[-1])
    while lista_valores!=[0]*len(lista_valores):
      valores_temporales=[]
      for i in range(1,len(lista_valores),1):
        valores_temporales.append(lista_valores[i]-lista_valores[i-1])
      lista_valores=valores_temporales.copy()
      diferencias.append(lista_valores[-1])
      tablas.append(lista_valores)
    suma_de_linea=0
    for numero in diferencias:
      suma_de_linea+=numero
    suma+=suma_de_linea
  print("Resultado:",suma)