#mi_diccionario = {"key1":<value1>,"key2":<value2>,"key3":<value3>,"key4":<value4>}
Persona = {"Nombre":"Iván","Apellido":"Latorre","Edad": 30, "Sueldo": 2020.45}
print(Persona)#diccionario completo
print(Persona["Edad"])#busca la clave y devuelve el valor
print(Persona["Sueldo"])
print("-----  Actualizar valores ----")
Persona["Edad"]=40 # Actualizar el diccionario
print(Persona)
print("----- Eliminar ------")
del Persona["Edad"]
print(Persona)
print("----- Buscar si existe información -----")
print(Persona.get("Apellido","Ninguno"))#cuando encuentra la etiqueta muestra el valor
print(Persona.get("Apellidos","Clave no encontrada"))#Muestra el segundo valor por no encontrar apellidos
print("----- Saber las key y claves del diccionario -----")
print(Persona.keys())
print(Persona.values())


