from time import perf_counter
inicio=perf_counter()
with open ("dia4.txt","r") as f:
  lineas=f.readlines()
  suma=0
  for i,linea in enumerate(lineas):
    lineas[i]=linea.rstrip()
  for linea in lineas:
    linea=linea[linea.index(":")+2:]
    ganadores,numeros=linea.split(" | ")[0].split(" "),linea.split(" | ")[1].split(" ")
    ganadores=[i for i in ganadores if i!=""]
    numeros=[i for i in numeros if i!=""]
    puntos=0
    for numero_ganador in ganadores:
      if numero_ganador in numeros:
        puntos=1 if puntos==0 else puntos*2
    suma+=puntos
  print("Resultado final",suma)
fin=perf_counter()
print("He tardado",fin-inicio,"segundos")