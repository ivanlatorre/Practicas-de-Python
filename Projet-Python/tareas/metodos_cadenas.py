cadena = "Estoy aprendiendo el lenguaje de programmación de Python"
print(cadena)
print("--- Buscar infomacion en la cadena ---")
print("lengiuaje esta en posición: ",cadena.find("lenguaje"))
print("Estoy esta en la posición: ", cadena.find(("Estoy")))
print("--- Cambiar: lower() y upper() ---")
print(cadena.lower())#fonts en formato minusculas
print(cadena.upper())#fonts en formato mayusculas
print(cadena.title())#priemera letra en posición en mayuscula
print(cadena.replace("aprendiendo", "desarrollando"))# reemplazarlo por otra infomación
print("--- Cortar ---")
print(cadena[6:16])#seleccion 16
print(cadena[6:17])#termina uno antes
print("--- Encontrar parte 2 find() ---")
print(cadena[:28].find("Python"))#limite de donde buscar resultado -1 no lo encontro

