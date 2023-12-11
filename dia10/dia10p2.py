with open("dia10.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]
  print("Este es el mapa:")
  for linea in lineas:
    print(linea)
  tuberias = {
    "|": (((0, 1), (0, 1)), ((0, -1), (0, -1))),
    "-": (((-1, 0), (-1, 0)), ((1, 0), (1, 0))),
    "L": (((0, 1), (1, 0)), ((-1, 0), (0, -1))),
    "J": (((0, 1), (-1, 0)), ((1, 0), (0, -1))),
    "7": (((0, -1), (-1, 0)), ((1, 0), (0, 1))),
    "F": (((0, -1), (1, 0)), ((-1, 0), (0, 1)))
  }
  misma_curva={"L":"J","J":"L","F":"7","7":"F"}
  for i,linea in enumerate(lineas):
    for j,caracter in enumerate(linea):
      if caracter=="S":
        pos_inicial=(j,i)
  #pos_inicial=(110,107)
  pasos=0
  bucle=[]
  posibles_direcciones=((1,0),(-1,0),(0,1),(0,-1))
  for posible_direccion in posibles_direcciones:
    print("Probamos por",posible_direccion)
    bucle=[pos_inicial]
    direcciones_del_bucle=[posible_direccion]
    try:
      pos=tuple(map(sum,zip(pos_inicial,posible_direccion)))
      print(pos)
      viene_de=posible_direccion
      pasos=1
      while lineas[pos[1]][pos[0]]!="S":
        #print("Estoy en",lineas[pos[1]][pos[0]])
        #print("Y vengo de",viene_de)
        if lineas[pos[1]][pos[0]]==".":
          print("No hay na")
          break
        if pos[0]<0 or pos[1]<0:
          raise IndexError
        for opcion in tuberias[lineas[pos[1]][pos[0]]]:
          if opcion[0]==viene_de:
            nueva_dir=opcion[1]
            break
        else:
          print("BONK")
          break
        bucle.append(pos)
        viene_de=nueva_dir
        pos=tuple(map(sum,zip(pos,nueva_dir)))
        pasos+=1
      else:
        print("He vuelto a S sano y salvo en",pasos,"pasos :D")
        direcciones_del_bucle.append(tuple([i*-1 for i in viene_de]))
        break
    except IndexError:
      print("Me he salido del mapa :(")
      continue
  direcciones_tuberia={((-1,0),(0,-1)):"J",((-1,0),(0,1)):"7",((-1,0),(1,0)):"-",((0,-1),(0,1)):"|",((0,-1),(1,0)):"L",((0,1),(1,0)):"F"}
  lineas[pos_inicial[1]]=lineas[pos_inicial[1]][:pos_inicial[0]]+direcciones_tuberia[tuple(sorted(direcciones_del_bucle))]+lineas[pos_inicial[1]][pos_inicial[0]+1:]
  print("He cambiado la S por",direcciones_tuberia[tuple(sorted(direcciones_del_bucle))])
  print("Te escribo un archivo con el mapa en el que está solo el bucle")
  with open("mapa_limpio.txt","w") as u:
    for i,linea in enumerate(lineas):
      for j,caracter in enumerate(linea):
        if (j,i) in bucle:
          u.write(caracter)
        else:
          u.write(".")
      u.write("\n")
  suma=0
  print("Y ahora, calculo los elementos dentro (I) y fuera (O) del bucle (te lo dejo en un mapa también))")
  #La magia detrás de esto es el teorema de Jordan, que dice que si trazas una línea desde un punto fuera de una figura cerrada hasta otro punto fuera de la figura, y cuentas las intersecciones que hace con la figura, si el número de intersecciones es impar, el punto está dentro de la figura, y si es par, está fuera.
  with open("resultados.txt","w") as o:
    for i,linea in enumerate(lineas):
      for j,caracter in enumerate(linea):
        if j==len(linea)-1:
          break
        if (j,i) not in bucle:
          intersecs=0
          curvas="JLF7"
          caracteres_de_intersec="|"+curvas
          #print(f"Miramos({j}, {i}), que es {lineas[i][j]}")
          for k in range(j+1,len(linea)): #Miramos a la derecha
            if lineas[i][k] in caracteres_de_intersec and (k,i) in bucle:
              if lineas[i][k] in curvas:
                caracteres_de_intersec="|"+lineas[i][k]+misma_curva[lineas[i][k]] #Una vez encontramos la primera curva, solo contamos las barras y las curvas en esa dirección
                curvas="" #Para no añadir más curvas de tipo distinto a la primera
                #print("Primera curva:",lineas[i][k])
                intersecs+=1
              else:
                intersecs+=1
                #print("Cuento",lineas[i][k],"como intersec")
          if intersecs%2==1:
            #print(f"({j}, {i}), que es {lineas[i][j]} es interno")
            suma+=1
            o.write("I")
          else:
            o.write("O")
        else:
          o.write(caracter)
      o.write("\n")
  print()
  print("El resultado (elementos dentro del bucle) es:",suma)

