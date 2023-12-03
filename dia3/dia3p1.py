def es_parte(lineas,linea,ini,fin,imprimir=True):
  if imprimir:
    print("Examinando",lineas[linea][ini:fin+1])
  lineas_a_examinar=[linea]
  nuevo_ini=ini-1*int(ini>0)
  nuevo_fin=fin+1*int(fin<len(lineas[linea])-1)
  if linea>0:
    lineas_a_examinar.insert(0,linea-1)
  if linea<len(lineas)-1:
    lineas_a_examinar.append(linea+1)
  if imprimir:
    for l in lineas_a_examinar:
      print(lineas[l][nuevo_ini:nuevo_fin+1])
  for l in lineas_a_examinar:
    for i in range(nuevo_ini,nuevo_fin+1):
      if lineas[l][i] not in ".0123456789":
        if imprimir:
          print("Es pieza")
        return True
  if imprimir:
    print("No es pieza")
  return False
with open("dia3.txt","r") as f:
  lineas=f.readlines()
  suma=0
  for i,linea in enumerate(lineas):
    lineas[i]=linea.replace("\n","")
  for i,linea in enumerate(lineas):
    numero=""
    inicio=None
    for j,caracter in enumerate(linea):
      if caracter.isdigit():
        if inicio is None:
          inicio=j
        numero+=caracter
      elif j>0 and linea[j-1].isdigit():
        if es_parte(lineas,i,inicio,j-1):
          suma+=int(numero)
        numero=""
        inicio=None
    if numero!="":
      if es_parte(lineas,i,inicio,len(linea)-1):
          suma+=int(numero)
  print("\n")
  print(suma)
