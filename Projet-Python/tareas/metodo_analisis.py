cadena = "Curso de Aprendizaje de Python"
print(cadena.count("de"))#cuanta cuantas veces aparece el contenido
print(cadena.find("de"))# busqueda de izquierda a derecha
print(cadena.rfind("de"))# busqueda de derecha a izquierda
print(cadena.startswith("Curso"))#pregunta si esta en esa posición respuesta booleana
print(cadena.endswith("Curso"))#pregunta si se encuentra al finalizar
print("----- SEPARADOR -----")
numero = "125"
print(numero.isnumeric())# ese contenido es numerico pero en string
numero2 = "abc"
print(numero2.isnumeric())
print(numero.isdigit())# pregunta si exciste datos numéricos
print(numero2.isdigit())
numero3 = "1234555"
print(numero3.isdigit())#true
print("---- alfanumérico ----")

cadena2 = "123455ddedeasd"
cadena3 = "1234%%dasda"
print(cadena2.isalnum())#dato alfanumérico letras y numeros simbolos y espacio de false
print(cadena3.isalnum())
print("----- datos alfabéticos")
abecedario = "zaabcdef"
print(abecedario.isalpha())#datos alfabéticos
abecedario2 = "1zaabcdef"
print(abecedario2.isalpha())#falso por dato numérico




