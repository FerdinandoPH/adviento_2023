cadena=".##.###"
lista_con_puntos = cadena.split('#')

# Filtrar los elementos vacíos (puntos)
lista_sin_puntos = list(filter(None, lista_con_puntos))

print(lista_sin_puntos)