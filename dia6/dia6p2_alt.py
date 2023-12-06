#Versión alternativa usando ✨mates✨ (más rápida)
with open("dia6.txt","r") as f:
  lineas=[x.rstrip() for x in f.readlines()]
  tiempo=int("".join(lineas[0][11:].split()))
  distancia=int("".join(lineas[1][11:].split()))
  print(tiempo)
  print(distancia)
  intersecciones=(int(((-tiempo+(tiempo**2+4*-distancia)**(1/2))/-2)),int(((-tiempo-(tiempo**2-4*-1*-distancia)**(1/2))/-2)))
  print("Resultado:",max(intersecciones)-min(intersecciones))