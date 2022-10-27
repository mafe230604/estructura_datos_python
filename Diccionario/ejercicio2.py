 #EJERCICIOS DICCIONARIOS

# Métodos propios

# El tipo de dato diccionario en Python posee una serie de funciones que nos permiten manipular los diccionarios realizando operaciones complejas de forma fácil y con una simple instrucción.


dayweekenglish={"Lunes": "Monday", "Martes": "Tuesday","Miércoles": "Wednesday","Jueves": "Thursday","Viernes": "Friday",}
print("Diccionario original: ", dayweekenglish)

# Función copy: realiza una copia exacta del diccionario en uno nuevo

diccionariocopia=dayweekenglish.copy()
print("Diccionario Copy: ", diccionariocopia)

# Función pop: obtiene el valor de la clave pasada como parámetro y además elimina el elemento del diccionario.

print("Valor del Lunes(pop): ", dayweekenglish.pop("Lunes"))
print("Diccionario después del pop: ", dayweekenglish)


# Función popitem: obtiene un elemento aleatorio del diccionario y loelimina del mismo.

print("Elemento al azar con popitem: ", dayweekenglish.popitem())
print("Diccionario después del popitem: ", dayweekenglish)


# Función get: obtiene el valor de la clave pasada como parámetro

print("Valor del Martes (get): ", dayweekenglish.get("Martes"))
print("Valor del Lunes (get) (no existe): ", dayweekenglish.get("Lunes"))
print("Valor del Lunes (get) (no existe): ", dayweekenglish.get("Lunes", "No existe"))

# Función update: realiza una actualización del diccionario usando otro diccionario. Aquellos elementos del diccionario que se utilizan para actualizar el principal sitituirán los existentes en el mismo y aquellos elementos que no existan serán añadidos al diccionario como nuevos elementos.

dayweekenglish.update({"Lunes": "MondayNUEVO", "Martes":"TuesdayNUEVO"})
print("Diccionario después del update: ", dayweekenglish)

# Función setdefault: intenta insertar un elemento(clave y valor) en el diccionario. En caso de no existir dicho elemento, la funcipon inserta y devuelve el valor del elemento y en caso de existir, lo único que hace es devolver el valor actual.

print("setdefault del Sábado. ", dayweekenglish.setdefault("Lunes", "Lunes"))
print("Diccionario después del setdefault(elemento existente): ", dayweekenglish)


# Función items: devuelve un objeto iterable(que puede usarse en bucles) compuesto por todos los elementos del diccionario.

print("Elemento iterable(items): ", dayweekenglish.items())


# Función keys: devuelve un objeto no iterable compuesto por todas las claves del diccionario.

print("Elemento iterable(claves): ", dayweekenglish.keys())


# Función values: devuelve un objeto iterable compuesto por todos los valores del diccionario

print("Elemento iterable(valores): ", dayweekenglish.keys())

# Función clear: elimina todos los lementos del diccionario
print("Diccionario después del clear: ", dayweekenglish.clear() )