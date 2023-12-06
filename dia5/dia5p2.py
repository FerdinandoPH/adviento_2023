with open("dia5.txt","r") as f:
    lineas_frozen=f.readlines()
    lineas=[]
    for i,linea in enumerate(lineas_frozen):
        if linea.strip() !="":
            lineas.append(linea.rstrip())
    rangos_de_mapeado=[]
    datos_iniciales=list(map(int,lineas[0].split(":")[1].split()))
    print(datos_iniciales)
    rangos_de_semillas=[]
    for i in range(0,len(datos_iniciales),2):
        rangos_de_semillas.append((datos_iniciales[i],datos_iniciales[i]+datos_iniciales[i+1]))
    print(rangos_de_semillas)
    subrangos_de_mapeado=[]
    for i, linea in list(enumerate(lineas))[2:]:
        if linea[0].isdigit():
            valores=linea.split(" ")
            subrangos_de_mapeado.append(list(map(int,linea.split())))
        else:
            rangos_de_mapeado.append(subrangos_de_mapeado)
            subrangos_de_mapeado=[]
    print(rangos_de_mapeado)
    nuevos_rangos_de_semillas=[]
    for subrango in rangos_de_mapeado:
        while len(rangos_de_semillas)>0:
            ini,fin=rangos_de_semillas.pop()
            for dest,src,long in subrango:
                inicio_intersec=max(ini,src)
                fin_intersec=min(fin,src+long)
                if inicio_intersec<fin_intersec:
                    print(f"Hay una intersección con {ini,fin} y {src,src+long} que tiene como src {src}")
                    nuevos_rangos_de_semillas.append((inicio_intersec-src+dest,fin_intersec-src+dest))
                    if inicio_intersec>ini:
                        rangos_de_semillas.append((ini,inicio_intersec))
                    if fin>fin_intersec:
                        rangos_de_semillas.append((fin_intersec,fin))
                    break
            else:
                nuevos_rangos_de_semillas.append((ini,fin))
            print(nuevos_rangos_de_semillas)
        rangos_de_semillas=nuevos_rangos_de_semillas.copy()
        nuevos_rangos_de_semillas=[]
    print("Resultado:",min(rangos_de_semillas)[0])

    #print(rangos)