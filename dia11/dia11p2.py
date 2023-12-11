from colorama import Fore
def detectar_columnas_vacias(lineas):
  frozen_lineas=tuple(lineas)
  columnas_vacias=[]
  for i in range(len(frozen_lineas[0])):
    if frozen_lineas[0][i]==".":
      for j in range(len(frozen_lineas)):
        if frozen_lineas[j][i]!=".":
          break
      else:
        columnas_vacias.append(i)
    else:
      continue
  return columnas_vacias
def detectar_filas_vacias(lineas):
  frozen_lineas=tuple(lineas)
  filas_vacias=[]
  for i in range(len(frozen_lineas)):
    for j in range(len(frozen_lineas[0])):
      if frozen_lineas[i][j]!=".":
        break
    else:
      filas_vacias.append(i)
  return filas_vacias
with open("dia11.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]

  galaxias=[]
  col_vacias=detectar_columnas_vacias(lineas)
  fil_vacias=detectar_filas_vacias(lineas)
  for i,linea in enumerate(lineas):
    for j,caracter in enumerate(linea):
      if j in col_vacias and i in fil_vacias:
        print(Fore.GREEN+caracter,end="")
      elif j in col_vacias:
        print(Fore.BLUE+caracter,end="")
      elif i in fil_vacias:
        print(Fore.RED+caracter,end="")
      else:
        print(Fore.WHITE+caracter,end="")
    print()
  print("Columnas vacías:",col_vacias)
  print("Filas vacías:",fil_vacias)
  for i,linea in enumerate(lineas):
    for j,caracter in enumerate(linea):
      if caracter=="#":
        galaxias.append((j,i))
  suma_de_distancias=0
  espaciador=999999 #tiene que ser -1 a la expansión desesada, excepto si es 1, entonces es 1
  for i in range(len(galaxias)-1,-1,-1):
    for j in range(i-1,-1,-1):
      #print("Para las galaxias",galaxias[i],"y",galaxias[j],":",set(range(min(galaxias[i][0],galaxias[j][0]),max(galaxias[i][0],galaxias[j][0])+1)).intersection(col_vacias),"en x y",set(range(min(galaxias[i][1],galaxias[j][1]),max(galaxias[i][1],galaxias[j][1])+1)).intersection(fil_vacias),"en y")
      distancia=(abs(max(galaxias[i][0],galaxias[j][0]) +espaciador*len(set(range(min(galaxias[i][0],galaxias[j][0]),max(galaxias[i][0],galaxias[j][0])+1)).intersection(col_vacias)) - min(galaxias[j][0],galaxias[i][0]))+abs(max(galaxias[i][1],galaxias[j][1])+espaciador*len(set(range(min(galaxias[i][1],galaxias[j][1]),max(galaxias[i][1],galaxias[j][1])+1)).intersection(fil_vacias)) -min(galaxias[j][1],galaxias[i][1])))
      #print("La distancia en x es de",abs(max(galaxias[i][0],galaxias[j][0]) +espaciador*len(set(range(min(galaxias[i][0],galaxias[j][0]),max(galaxias[i][0],galaxias[j][0])+1)).intersection(col_vacias)) - min(galaxias[j][0],galaxias[i][0])),"y la distancia en y es de",abs(max(galaxias[i][1],galaxias[j][1])+espaciador*len(set(range(min(galaxias[i][1],galaxias[j][1]),max(galaxias[i][1],galaxias[j][1])+1)).intersection(fil_vacias)) -min(galaxias[j][1],galaxias[i][1])),"dando un total de",distancia)
      suma_de_distancias+=distancia
      
  print("Resultado (suma de las distancias entre galaxias):",suma_de_distancias)
