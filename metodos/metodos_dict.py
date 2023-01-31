diccionario = {
    "nombre"   : 'Ivan',
    "apellido" : 'Lato',
    "perros"   :  4
}
print("----- keys -----")
claves = diccionario.keys()#devuelve una lista con las claves del diccionario#solo sirve para iterar
print("claves diccionario key: ",claves)
print("------ get -----")
claves = diccionario.get("perros")
print("diccionario con get: ",claves)#devuelve el valor de la clave
#Si la clave no está en el diccionario, devuelve default o None si no se especifica ningún valor.
claves = diccionario["nombre"]
print("claves = diccionario['nombre']",claves)
claves = diccionario.get("none")
print("claves de get no encontrada, ",claves)#devuelve none cuando no existe la key
print("------ clear -----")
#eliminando = diccionario.clear()
#print("clear: ",eliminando)
print("----- pop ------")# Elimina el elemento con la clave especificada y devuelve su valor. Si la clave no está en el diccionario, devuelve default o produce un error si no se especifica ningún valor.
print(diccionario)
diccionario_pop = diccionario.pop("nombre")#varios elementos
print("eliminando elemento",diccionario_pop)
print(diccionario)
print("------- items -------")
#Devuelve una lista de tuplas con los pares clave-valor del diccionario.
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
