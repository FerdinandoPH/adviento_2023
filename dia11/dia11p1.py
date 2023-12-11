def expandir_columnas(lineas):
  frozen_lineas=tuple(lineas)
  compensador=0
  for i in range(len(frozen_lineas[0])):
    if frozen_lineas[0][i]==".":
      for j in range(len(frozen_lineas)):
        if frozen_lineas[j][i]!=".":
          break
      else:
        for j in range(len(frozen_lineas)):
          lineas[j]=lineas[j][:i+compensador]+"."+lineas[j][i+compensador:]
        compensador+=1
    else:
      continue
  return lineas
def expandir_filas(lineas):
  frozen_lineas=tuple(lineas)
  compensador=0
  for i in range(len(frozen_lineas)):
    for j in range(len(frozen_lineas[0])):
      if frozen_lineas[i][j]!=".":
        break
    else:
      lineas.insert(i+compensador,"."*len(lineas[0]))
      compensador+=1
  return lineas
with open("dia11.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]
  for linea in lineas:
    print(linea)
  print()
  lineas=expandir_columnas(lineas)
  lineas=expandir_filas(lineas)
  for linea in lineas:
    print(linea)
  galaxias=[]
  for i,linea in enumerate(lineas):
    for j,caracter in enumerate(linea):
      if caracter=="#":
        galaxias.append((j,i))
  suma_de_distancias=0
  for i in range(len(galaxias)-1,-1,-1):
    for j in range(i-1,-1,-1):
      suma_de_distancias+=(abs(galaxias[i][0]-galaxias[j][0])+abs(galaxias[i][1]-galaxias[j][1]))
  print("Resultado (suma de las distancias entre galaxias):",suma_de_distancias)
