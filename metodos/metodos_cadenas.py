cadena1 = "Hola sr Iván Lato dev web"
cadena2 = "Bienvenido Maquina"
print("----- DIR -----")

print("dir en cadena: ",dir(cadena1))# muestra lo que podemos hacer con ese objeto
print("----- DIR -----")
print("dir en int: ",dir(4))
print("----- DIR -----")
print("dir en float: ",dir(5.5))
print("----- DIR -----")
print("dir en lista: ",dir(["ivan","mas",5]))
print("----- UPPER -----")#Mayusculas
mayusc = cadena1.upper()
print(mayusc)
print("----- LOWER -----")#Mínusculas
minusc = cadena1.lower()
print(minusc)
print("-----Capitaliza -----")#primeras letras en mayusculas y las demas en minusculas
primeras_letras_en_mayusc = cadena1.capitalize()
print(primeras_letras_en_mayusc)
print("----- FIND -----")
busqueda_find = cadena1.find("Hola")
print("Busqueda con find: ",busqueda_find)#posición en donde lo encuentra
busqueda_find2 = cadena1.find("a")
print("Busqueda con find: ",busqueda_find2)
busqueda_find3 = cadena1.find("z")
print("Busqueda con find: ",busqueda_find3)#valor -1 cuando no encuentra nada


