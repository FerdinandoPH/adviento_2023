with open("dia8.txt","r") as f:
  lineas=[i.rstrip() for i in f.readlines()]
  direcciones=lineas[0]
  mapa={}
  for i in range(2,len(lineas)):
    rumbos=tuple((lineas[i][lineas[i].index("(")+1:len(lineas[i])-1].split(", ")[0],lineas[i][lineas[i].index("(")+1:len(lineas[i])-1].split(", ")[1]))
    mapa[lineas[i].split(" = ")[0]]=rumbos
  print(mapa)
  print(direcciones)
  pasos=0
  lugar_actual="AAA"
  while lugar_actual!="ZZZ":
    #print(mapa[lugar_actual],"y tengo que ir por",direcciones[pasos%len(direcciones)])
    if direcciones[pasos%len(direcciones)]=="L":
      lugar_actual=mapa[lugar_actual][0]
    else:
      lugar_actual=mapa[lugar_actual][1]
    pasos+=1
  print("Resultado:",pasos)