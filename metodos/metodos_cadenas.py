cadena1 = "Hola sr Iván Lato dev web"
cadena2 = "BienvenidoMaquina"
cadena3 = "152256456"
cadena4 = "12321asdas45612"
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
print("----- BUSQUEDA DE INDEX -----")
busqueda_index = cadena1.index("a")
print("busqueda por index: ",busqueda_index)
#busqueda_index2 = cadena1.index("z")
#print("busqueda por index: ",busqueda_index2)#error cunado no lo encuentra 
print("----- isnumeric -----")
es_numerico = cadena3.isnumeric()
es_numerico2 = cadena1.isnumeric()
print("cadena3 es numerico:",es_numerico)
print("cadena1 es numerico:",es_numerico2)
print("----- ISALPHA ----")
es_alfanumerico = cadena4.isalpha()
print("es alfanumerico cadena4: ",es_alfanumerico)
es_alfanumerico2 = cadena2.isalpha()#cadena 2 esta todo junto
print("es alfanumerico cadena2: ",es_alfanumerico2)
print("------ count -----")
contar_coincidencias = cadena1.count("a")
contar_coincidencias2 = cadena1.count("I")
contar_coincidencias3 = cadena1.count("i")
print('coincidencia cadena1: "a" :' ,contar_coincidencias)
print('coincidencia cadena1: "I" :' ,contar_coincidencias2)
#si no lo encuentra es 0
print('coincidencia cadena1: "i" :' ,contar_coincidencias3)
print("----- LEN -----")
contar_caracteres = len(cadena1)
print("len cadena1: ",contar_caracteres)
print("----- STARTWITH -----")
empieza_con = cadena1.startswith("H")
print("Empieza con H ",empieza_con)
print("----- ENDSWITCH -----")
termina_con = cadena1.endswith("a")
print("termina con b ",termina_con)
print("----- replace ------")
print(cadena2)
cadena_nueva = cadena2.replace("BienvenidoMaquina","Bienvenid@ Maquinola")
print("cadena2 con replace:",cadena_nueva)

print("----- split -----")
cadena_separada = cadena1.split()
print(cadena_separada)
cadena_separada2 = cadena1.split(".")
print(cadena_separada2)
print("cadena separada es: ",type(cadena_separada))


