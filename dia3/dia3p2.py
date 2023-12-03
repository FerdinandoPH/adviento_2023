from time import perf_counter
class Parte:
  def __init__(self,id,linea,ini,fin):
    self.id=id
    self.linea=linea
    self.ini=ini
    self.fin=fin
def es_parte(lineas,linea,ini,fin):
  print("Examinando",lineas[linea][ini:fin+1])
  lineas_a_examinar=[linea]
  nuevo_ini=ini-1*int(ini>0)
  nuevo_fin=fin+1*int(fin<len(lineas[linea])-1)
  if linea>0:
    lineas_a_examinar.insert(0,linea-1)
  if linea<len(lineas)-1:
    lineas_a_examinar.append(linea+1)
  for l in lineas_a_examinar:
    print(lineas[l][nuevo_ini:nuevo_fin+1])
  for l in lineas_a_examinar:
    for i in range(nuevo_ini,nuevo_fin+1):
      if lineas[l][i] not in ".0123456789":
        print("Es pieza")
        return True
  print("No es pieza")
  return False
def obtener_partes(lineas,linea,pos,lista_partes):
  partes_adjuntas=[]
  print("Pos es",pos)
  print("Condición es",pos<len(lineas[linea])-1)
  nuevo_ini=pos-1*int(pos>0)
  nuevo_fin=pos+1*int(pos<len(lineas[linea])-1)
  print(f"Rango es de {nuevo_ini} a {nuevo_fin}")
  lineas_a_examinar=[linea]
  if linea>0:
    lineas_a_examinar.insert(0,linea-1)
  if linea<len(lineas)-1:
    lineas_a_examinar.append(linea+1)
  for l in lineas_a_examinar:
    print(lineas[l][nuevo_ini:nuevo_fin+1])
  for l in lineas_a_examinar:
    for i in range(nuevo_ini,nuevo_fin+1):
      if lineas[l][i].isdigit():
        for parte in lista_partes:
          if parte.linea==l and i in range(parte.ini,parte.fin+1) and parte.id not in (p.id for p in partes_adjuntas):
            partes_adjuntas.append(parte)
  return partes_adjuntas
start=perf_counter()
with open("dia3.txt","r") as f:
  suma=0
  lineas=f.readlines()
  partes=[]
  num_partes=0
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
          num_partes+=1
          partes.append(Parte(num_partes,i,inicio,j-1))
        numero=""
        inicio=None
    if numero!="":
      if es_parte(lineas,i,inicio,len(linea)-1):
          num_partes+=1
          partes.append(Parte(num_partes,i,inicio,len(linea)-1))
  print("\n")
  print("Piezas:",end=" ")
  for parte in partes:
    print(lineas[parte.linea][parte.ini:parte.fin+1],end=",")
  print("\n")
  partes=sorted(partes,key=lambda x:x.linea)
  for i,linea in enumerate(lineas):
    for j,caracter in enumerate(linea):
      if caracter=="*":
        print(f"Engranaje en [{i+1},{j+1}]")
        partes_adjuntas=obtener_partes(lineas,i,j,partes)
        print("Partes adjuntas:",end=" ")
        for parte in partes_adjuntas:
          print(lineas[parte.linea][parte.ini:parte.fin+1],end=",")
        print("\n")
        multi=0
        if len(partes_adjuntas)==2:
          multi=1
          for parte in partes_adjuntas:
            multi*=int(lineas[parte.linea][parte.ini:parte.fin+1])
        print("Sumando",multi)
        suma+=multi
  print("El resultado es",suma)
end=perf_counter()
print("Tiempo de ejecución:",end-start,"segundos")