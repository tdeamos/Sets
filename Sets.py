################################################################################################################################
# Conjunto - Coleccion de elementos sin orden - # Lista - Coleccion de elementos ordenados, que pueden repetirse
################################################################################################################################

# Creacion de un conjunto
set1 = {1, 2, 3, 4}

# Impresion
print(set1)

# Mostrar datos mediante un breakpoint

# Los elementos pueden ser de distinto tipo
# booleanos, decimales, enteros, strings ....
# No se pueden anidar conjuntos
set2 = {True, 3.14, None, False, "Hola mundo", (1, 2)}
print(set2)

# Aplicada sobre un literal extrae los elementos unicos
set3 = set('abracadabra')
print(set3)

# Usando la funcion range para generar rangos de numeros
set4 = set(range(1,10))
print(set4)


################################################################################################################################
# Operaciones sobre conjuntos
################################################################################################################################

# Cardinalidad
set6 = {1, 2, 3}
print("Tamanio de set6: " + str(len(set6)))
print("Elementos de set6: " + str(set6))

# Pertenencia de un elemento a un conjunto
print("Pertenencia de un elemento a un conjunto")
print(3 in set6)

# Borrado de elementos
print("Borrado de elementos")
set6.clear()
print(set6)



### Borrar un elemento en especifico ? y agregarlo ?

################################################################################################################################
# Otros elementos de datos - Listas
################################################################################################################################

## Lista - Coleccion de elementos ordenados, que pueden repetirse
#text = "Hola chic@s!"
#print(list(text))
#print(set(text))
#
## Ordenamiento
## No tiene sentido en sets, solo en las listas
#
#lista = list(text)
#print(lista[1])
#
#set5 = set(text)
##print(set5[1])
