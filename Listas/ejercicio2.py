# EJECICIOS LISTAS

# Metodos propios 

lista =[45, 32, 3, 78]
print("listas original: ", lista)
# funcion append: añada un elemento de la lista 
lista.append(995)
lista.append(7)
print("lista despues de usar append: " , lista)
# Funcion sort: ordena la lista
lista.sort()
print("Lista ordenada: ", lista)
# Funcion reverse: invierte el orden de la lista
lista.reverse()
print("lista al reves:" , lista)
# Funcion extend:añade los elementos de una lista a la lista
lista_extend =[1,5,87,45]
lista.extend(lista_extend)
print("lista despues de extend: ", lista)
#Funcion count:cuentael numero de veses que aparece el elemento indicado como parametro dentro de la lista
print("numero de elementos 45: ", lista.count(45))
# Funcion insert:
lista.insert(4,111)
print("lista despues de inset", lista)
# Funcion remove:elimina la primera ocurrencia empezando por la  lista del elemento indicado como parametro.
lista.remove(45)
print("lista despues de remove: ", lista)
# Funcion index:devuelve la posicion de la primera ocurrencia de izquierda a derecha enla lista, delelemento pasadocomo parametro
print("posicion del elemento 111:" , lista.indix(111))
# Funcion pop:elimina el ultimo  elemento de la lista y lo devuelve como resultado de la operacion.
lista.pop()
print("lista despues de pop:" , lista)
# Funcion clear:elimina todos los elementos de la lista
lista.clear()
print("lista despues de clear" ,lista)