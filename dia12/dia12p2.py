with open("dia12prac.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]
  suma=0
  for i,linea in enumerate(lineas,1):
    print(f"Progreso: {i}/{len(lineas)}",end="\r")
    partes=linea.split(" ")[0]
    #print(partes)
    partes+=4*("?"+partes)
    #print(partes)
    descripciones=[int(x) for x in linea.split(" ")[1].split(",")]
    descripciones*=5
    #print(descripciones)
    interrogaciones=partes.count("?")
    #print(interrogaciones)
    for i in range(2**interrogaciones):
      partes_temporal=partes
      variacion = bin(i)[2:].rjust(interrogaciones, '0')
      #print(s)
      variacion = variacion.replace('0', '.')
      variacion = variacion.replace('1', '#')
      #print(s)
      for caracter in variacion:
        partes_temporal=partes_temporal.replace("?",caracter,1)
      #print(partes_temporal)
      regiones_rotas=[x.count("#") for x in list(filter(None,partes_temporal.split(".")))]
      #print(regiones_rotas)
      if regiones_rotas==descripciones:
        suma+=1
  print("Resultado (suma de las posibilidades de colocación):",suma)