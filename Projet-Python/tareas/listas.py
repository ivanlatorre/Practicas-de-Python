"""
Las listas se pueden modificar
"""

Contenido = ["Cursos", "Alumnos", 1025,True,105.38,"Masculino"]
print(Contenido)
Contenido[1]="Estudiantes"#cambio
print(Contenido)
print(Contenido[3])
print(Contenido[-1])#imprime el ultimo contenido
print(Contenido[0:3])#toma los elementos seleccionados
print(Contenido[:2])# [:2]toma los elementos desde la posicion 0

print("----- Listas Agregados ----")
Contenido.append("Python")
print([Contenido])#dato agregado al final
print("----- Lista Icertar datos -----")
Contenido.insert(2,"Profesor")# dato incertado en la posición 2
print(Contenido)
print("----- Extend -----")
Contenido.extend(["Nivel Básico", "Nivel Intermedio", "Nivel Avanzado"])
print(Contenido)#agrega al final de la lista
print("----- Consulta de elementos -----")
print(Contenido.index("Masculino"))
print("----- Eliminar Contenido -----")
Contenido.remove("Masculino")
print(Contenido)
Contenido.remove(1025)
print(Contenido)
print("----- Contar Elementos -----")
print(Contenido.count(105.38))
Contenido.append("Cursos")
print(Contenido.count("Cursos"))#Curso X2
Contenido2 = ["Curso1","Curso2"]
Resultado = Contenido+Contenido2
print(Resultado)
