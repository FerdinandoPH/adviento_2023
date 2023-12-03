from time import perf_counter
with open("dia2.txt", "r") as f:
    start_time=perf_counter()
    lineas=f.readlines()
    suma=0
    for linea in lineas:
      linea=linea[linea.index(":")+2:]
      partidas=linea.split("; ")
      colores={"red":0,"green":0,"blue":0}
      for partida in partidas:
         dados=partida.split(", ")
         for dado in dados:
            dato_del_dado=dado.split(" ")
            if int(dato_del_dado[0])>colores[dato_del_dado[1].rstrip()]:
               colores[dato_del_dado[1].rstrip()]=int(dato_del_dado[0])
      suma+=colores["red"]*colores["green"]*colores["blue"]
    print(suma)
    stop_time=perf_counter()
    print("Ha tardado: ",stop_time-start_time,"segundos")