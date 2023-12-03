from time import perf_counter
with open("dia2.txt", "r") as f:
    lineas=f.readlines()
    suma=0
    start_time=perf_counter()
    for i,linea in enumerate(lineas):
      es_posible=True
      linea=linea[linea.index(":")+2:]
      partidas=linea.split("; ")
      for partida in partidas:
         colores={"red":0,"green":0,"blue":0}
         dados=partida.split(", ")
         for dado in dados:
            dato_del_dado=dado.split(" ")
            colores[dato_del_dado[1].rstrip()]+=int(dato_del_dado[0])
         if colores["red"]>12 or colores["green"]>13 or colores["blue"]>14:
            es_posible=False
            break
      if es_posible:
         suma+=i+1
    print(suma)
    stop_time=perf_counter()
    print("Ha tardado: ",stop_time-start_time,"segundos")