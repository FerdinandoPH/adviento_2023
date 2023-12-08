from time import sleep
def determina_pares(mano):
  cartas={}
  rangos={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"T":11, "J":1,"Q":12,"K":13,"A":14}
  for carta in mano:
    cartas[carta]=cartas.get(carta,0)+1
  print(cartas)
  if "J" in cartas.keys() and len(cartas)>1:
    j_a_reemplazar=cartas["J"]
    del cartas["J"]
    max_valor = max(cartas.values())
    llaves_max_valor = [key for key, value in cartas.items() if value == max_valor]
    nuevo_diccionario = {key: value for key, value in cartas.items() if key in llaves_max_valor}
    llave=list(rangos.keys())[list(rangos.values()).index(max([rangos[i] for i in list(nuevo_diccionario.keys())]))]
    cartas[llave]+=j_a_reemplazar
    print("Por las J cambia a",cartas)
  valores={(5,):7,(1,4):6,(2,3):5,(1,1,3):4,(1,2,2):3,(1,1,1,2):2,(1,1,1,1,1):1}
  return valores[tuple(sorted(cartas.values()))]
with open("dia7.txt","r") as f:
  lineas=[l.rstrip() for l in f.readlines()]
  rangos={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"T":11, "J":1,"Q":12,"K":13,"A":14}
  manos={}
  manos_ordenadas={}
  for linea in lineas:
    manos[linea.split()[0]]=int(linea.split()[1])
  ranking_pares=[]
  for mano in manos.keys():
    ranking_pares.append(determina_pares(mano))
  manos = dict([x for _,x in sorted(zip(ranking_pares,manos.items()))])
  ranking_pares.sort()
  #print(manos)
  separadores=[idx for idx in range(1, len(ranking_pares)) if ranking_pares[idx] != ranking_pares[idx - 1]]
  separadores.insert(0,0)
  separadores.append(len(manos)+1)
  #print(separadores)
  for i in range(1,len(separadores)):
    subseccion=list(manos.items())[separadores[i-1]:separadores[i]]
    #print("Subseccion:",subseccion)
    while len(subseccion)>0:
      copia_subseccion=subseccion.copy()
      posicion=0
      while len(copia_subseccion)>1:
        candidatos=[]
        letras_a_comparar=[]
        #print("Copia subseccion",copia_subseccion)
        for mano in copia_subseccion:
          #print("Cogiendo el elemento",posicion,"de",mano)
          letras_a_comparar.append(mano[0][posicion])
        letra_a_comparar=min([rangos[x] for x in letras_a_comparar])
        #print("Fuera todo lo que sea mayor que",letra_a_comparar)
        for mano in copia_subseccion:
          #print(rangos[mano[0][posicion]],"vs",letra_a_comparar)
          if rangos[mano[0][posicion]]<=letra_a_comparar:
            candidatos.append(mano)
        copia_subseccion=candidatos.copy()
        posicion+=1
      #print(copia_subseccion)
      #print(copia_subseccion[0])
      manos_ordenadas[copia_subseccion[0][0]]=copia_subseccion[0][1]
      subseccion.remove(copia_subseccion[0])
  print("----FIN-----")
  print(manos_ordenadas)
  for i in range(len(separadores)):
    print(list(manos.items())[separadores[i-1]:separadores[i]+1*int(i==len(separadores)-1)])
    print("\n\n--------\n\n")
  suma=0
  for i,valor in enumerate(list(manos_ordenadas.values()),1):
    suma+=valor*i
  print(suma)

     