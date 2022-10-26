# en el siguiente ejercicio vamos a ver como definir una tupla y como acceder a sus elementos. El código es el siguiente:

tupla=("casa","2",345,"perro",99)
print("Elementos de la tupla: ", tupla)
print("Elemento de la posicion 0: ", tupla[0])
print("Elemento de la posicion 1: ", tupla[1])
print("Elemento de la posicion 2: ", tupla[2])
print("Elemento de la posicion 3: ", tupla[3])
print("Elemento de la posicion 4: ", tupla[4])

#funcion count: cuenta el umero de veces que parece el elemento indicado como parámetro dentro de la tupla
#funcion index:devuelve la posicion de la primera ocurrencia de izquierda a derecha en la tupla del elemento pasado como parámetro.

#A continuacion vamos a hacer realizar un ejercicio para aprender a utilizar ambas funciones de las tuplas. El codigo fuente es el siguiente:
tupla=("casa","2",99,345,"perro",99)
print("elementos de la tupla: ",tupla)
print("numero de elementos 99: ",tupla.count(99))
print("posicion que ocupa el elemento perro: ",tupla.index("perro"))

#la instruccion extraera una nueva tupla que empezara en el indice n y terminara en el m-1. Tienes que tener en cuenta lo siguiente:

#n siempre tiene que ser menor que m.
#si no se especifica el valor de n se supone que es 0.
#si no se especifica el valor para m se supone que es el tamaño de la lista menos uno.

#veamoslo en un ejercicio, el codigo fuente es el siguiente
tupla=(1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])

#tupla concatenada=tupla1+tupla2

#ademas, vamos a aprender a utilizar una funcion para conocer el numero de elementos que componen la tupla. dicha funcion se llama len y devuelve un entero que indica el numero de elementos que la componen. se utiliza de la siguiente manera:

#numeroElementos=len(tupla)
#el codigo fuente del ejercicio es el siguiente:

tupla1=(29,"television",8763)
tupla2=(1,2,3,"videojuego")
print("numero elementos de tupla1: ",len(tupla1))
print("tupla1: ",tupla1)
print("numero elementos de tupla2: ",len(tupla2))
print("tupla1: ",tupla2)
tuplaconcatenada=tupla1+tupla2
print("numero elementos de tuplaconcatenada: ",len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

#tuplaresultante=tupla*numeroentero
#la tupla resultante de la multiplicacion sera una tupla compuesta por tantas veces la tupla como valor tenga el numero entero.
#el codigo fuente del ejercicio es el siguiente:

tupla=(1,2,3,4,5,6,7,8,9,0)
print(tupla)
tuplaresultante=tupla*4
print(tuplaresultante)

