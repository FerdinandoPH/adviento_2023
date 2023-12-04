from time import perf_counter
inicio=perf_counter()
with open ("dia4.txt","r") as f:
  lineas=f.readlines()
  suma=0
  cantidad_mismo_id=1
  puntos=0
  fin_de_ids={}
  for i,linea in enumerate(lineas):
    lineas[i]=linea.rstrip()
    fin_de_ids[i+1]=i
  lineas_congeladas=lineas.copy()
  max_id=int(list(fin_de_ids.keys())[-1])
  print(fin_de_ids)
  for i,linea in enumerate(lineas):
    id=int(linea[linea.index(" ")+1:linea.index(":")])
    try:
      siguiente_id=int(lineas[i+1][lineas[i+1].index(" ")+1:lineas[i+1].index(":")])
    except IndexError:
      siguiente_id=id+1
    if siguiente_id>id:
      print("Cambio al id:",id,"inminente")
      linea_a_examinar=linea[linea.index(":")+2:]
      ganadores,numeros=linea_a_examinar.split(" | ")[0].split(" "),linea_a_examinar.split(" | ")[1].split(" ")
      ganadores=[k for k in ganadores if k!=""]
      numeros=[k for k in numeros if k!=""]
      puntos=0
      for numero_ganador in ganadores:
        if numero_ganador in numeros:
          puntos+=1
      nuevas_cartas=range(id+1,id+puntos+1)
      print("Nuevas cartas a meter:",nuevas_cartas,"*",cantidad_mismo_id)
      for nueva_carta in nuevas_cartas:
        for j in range(cantidad_mismo_id):
          lineas.append(lineas_congeladas[nueva_carta-1])
      lineas.sort()
      cantidad_mismo_id=1
    else:
      cantidad_mismo_id+=1
  print("Resultado final",len(lineas))
fin=perf_counter()
print("He tardado",fin-inicio,"segundos")