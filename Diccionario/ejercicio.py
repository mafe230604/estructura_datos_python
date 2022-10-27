# EJERCICIOS DICCIONARIOS

# Ejercicios manipulación

# 1. Consiste en crear un diccionario y mostrar algunos elementos del mismo,accediendo a ellosusando la clave del elemento.
print("------Ejercicio 1-------")
dayweekenglish={"Lunes": "Monday", "Martes": "Tuesday","Miércoles": "Wednesday","Jueves": "Thursday","Viernes": "Friday",}
print(dayweekenglish)
print(dayweekenglish["Lunes"])
print(dayweekenglish["Miércoles"])
print(dayweekenglish["Viernes"])


# 2. Consiste en añadir elementos al diccionario, eliminar y modificar el valor de los elementos del mismo.
print("------Ejercicio 2-------")
dayweekenglish={"Lunes": "Monday", "Martes": "Tuesday","Miércoles": "Wednesday","Jueves": "Thursday","Viernes": "Friday",}
print(dayweekenglish)
dayweekenglish["Sabado"]="Saturday"
print(dayweekenglish)
dayweekenglish["Domingo"]="Sunday"
print(dayweekenglish)
dayweekenglish["Lunes"]="MondayBORRAR"
print(dayweekenglish)
del dayweekenglish["Lunes"]
print(dayweekenglish)

# 3. Usar len, min y max para obtener el númerod e elemntos del diccionario, el menor valor y el mayor valor, respectivamente.
print("------Ejercicio 3-------")

dayweekenglish={"Lunes": "Monday", "Martes": "Tuesday","Miércoles": "Wednesday","Jueves": "Thursday","Viernes": "Friday"}
print("Número de elementos del diccionario: ", len(dayweekenglish))
print("Elemento mayor del diccionario: ", max(dayweekenglish))
print("Elemento menor del diccionario: ", min(dayweekenglish))
