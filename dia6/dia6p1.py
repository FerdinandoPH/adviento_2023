with open("dia6.txt","r") as f:
  lineas=[x.rstrip() for x in f.readlines()]
  tiempos=[int(x) for x in lineas[0][11:].split()]
  distancias=[int(x) for x in lineas[1][11:].split()]
  suma=0
  for i,tiempo in enumerate(tiempos):
    posibilidades=0
    print("Tiempo:",tiempo)
    for j in range(1,tiempo):
      #print(f"{tiempo-j}*{j}={(tiempo-j)*j}, que comparo con {distancias[i]}")
      if (tiempo-j)*j>distancias[i]:
        posibilidades+=1
    print("Hay",posibilidades,"posibilidades")
    suma=posibilidades if suma==0 else suma*posibilidades
  print(suma)