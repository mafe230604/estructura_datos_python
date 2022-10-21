# EJECICIOS VISTAS

# EJERCICIOS MANIPULACIÓN

# 1. Consiste en la definición de una lista con elementos de diferentes tipos y en mostrarla por pantalla, tanto entera como por elementos accediendo ala posición que ocupa dentro dela lista.
lista = ["Python", "Gaunenta", 2022, "Libro",]
print (lista)
print (lista[0])
print(lista[2])

# 2. Consiste en el uso del operador + para realizar uniones de listas. Además la función len para conocer el número de elementos que componen la lista.
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
lista2 = ["Abrigo", "Jersey", "Sudadera", "Calcetines"]
print("Número elementos lista1: ", len(lista1))
print("lista1:", lista1)
print("Número elementos lista2: ", len(lista2))
print("lista2: ", lista2)
lista_concatenada = lista1 + lista2
print("Número elementos lista concatenada: ", len(lista_concatenada))
print("lista_concatenada: ", lista_concatenada)

# 3. Añadir elementos a la lista de diferentes formas 
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["Jersey", "Sudadera"]
print(lista)
lista = lista + ["Calcetines"] + ["Bufanda"]
print(lista)

# 4. Modificar elementos de una lista y borrar elementos de la misma 
lista1 = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista[1] = "Cazadora"
print(lista)
del lista[0]
print(lista)

#5. Uso del operador *. permite concatenar uan lista con ellas misma un numero finito de veces.
lista = ["Camiseta", "Pantalon", "Zapatillas"]
print(lista)
lista_resultado =lista* 3
print(lista_resultado)

# 6. Creacin de lsitas como elementos de listas y acceso a dicho elemento .
print("--------Ejercicio 6")
lista =["camiseta", ["calcetines", "Cazadores"],"Zapatos"]
print (lista[0])
print (lista[1])
print (lista[2])
print (lista[1][0])
print (lista[1][1])

# 7. Extraer uan porcion de las listas en una lista nueva.
print("-------Ejercicio 7-------")
listas=[1,2,3,4,5,6,7,8,9]
print(listas)
listal1 =listas[3:7]
print(lista1)
lista2 =lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)
