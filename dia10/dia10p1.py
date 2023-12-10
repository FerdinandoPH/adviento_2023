
with open("dia10.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]
  tuberias = {
    "|": (((0, 1), (0, 1)), ((0, -1), (0, -1))),
    "-": (((-1, 0), (-1, 0)), ((1, 0), (1, 0))),
    "L": (((0, 1), (1, 0)), ((-1, 0), (0, -1))),
    "J": (((0, 1), (-1, 0)), ((1, 0), (0, -1))),
    "7": (((0, -1), (-1, 0)), ((1, 0), (0, 1))),
    "F": (((0, -1), (1, 0)), ((-1, 0), (0, 1)))
  }
  for i,linea in enumerate(lineas):
    for j,caracter in enumerate(linea):
      if caracter=="S":
        pos_inicial=(j,i)
  pasos=0
  posibles_direcciones=((1,0),(-1,0),(0,1),(0,-1))
  print(pos_inicial)
  for posible_direccion in posibles_direcciones:
    print("Probamos por",posible_direccion)
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
        viene_de=nueva_dir
        pos=tuple(map(sum,zip(pos,nueva_dir)))
        pasos+=1
      else:
        print("He vuelto a S sano y salvo en",pasos,"pasos :D")
        break
    except IndexError:
      print("Me he salido del mapa :(")
      continue
  print("Pasos del trayecto exitoso:")
  print(pasos)
  print("Resultado (casilla del bucle más lejana):",pasos//2)
