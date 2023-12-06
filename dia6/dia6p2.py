with open("dia6.txt","r") as f:
  lineas=[x.rstrip() for x in f.readlines()]
  tiempo=int("".join(lineas[0][11:].split()))
  distancia=int("".join(lineas[1][11:].split()))
  posibilidades=0
  print(tiempo)
  print(distancia)
  for i in range(1,tiempo):
    if (tiempo-i)*i>distancia:
      posibilidades+=1
  print(posibilidades)