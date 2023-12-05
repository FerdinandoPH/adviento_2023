with open("dia5.txt","r") as f:
    lineas_frozen=f.readlines()
    lineas=[]
    for i,linea in enumerate(lineas_frozen):
        if linea.strip() !="":
            lineas.append(linea.rstrip())
    categorias={}
    for i,linea in enumerate(lineas):
        if not linea[0].isdigit():
            categorias[linea]=i
    semillas=lineas[0][7:].split(" ")
    for i,semilla in enumerate(semillas):
        semillas[i]=int(semilla)
    print(semillas)
    rangos={}
    for i,linea in enumerate(lineas):
        if i in list(categorias.values()) and i>1:
            print("Rangos: ",rangos)
            for j,semilla in enumerate(semillas):
                for rango in rangos.keys():
                    if semilla in rango:
                        semillas[j]-=rangos[rango]
            print("Nuevas semillas:",semillas)
            rangos={}
        elif i>1:
            valores=linea.split(" ")
            rangos[range(int(valores[1]),int(valores[1])+int(valores[2]))]=int(valores[1])-int(valores[0])
    print("Semillas finales:",semillas)
    print("Semilla más cercana:",min(semillas))