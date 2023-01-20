#Entrda de teclado
#input("Ingrese su Nombre: ")#finaliza al ingresar respuesta del teclado
cNombre = input("Ingrese su Nombre: ") #la entrada se guarda en la varible
nEdad = input("Ingrese su Edad: ")
#convertir un dato string a int
nSueldo = int(input("Ingrese su Sueldo: ")) + 500 #operaciones
#convertir int a float
nSueldo2 = float(input("Ingrese sueldo en decimales: ")) + 0.35


print("Su nombre es: ",cNombre)
print("Su edad es :",nEdad)
print("Su sueldo base + 500 es: ",nSueldo)
print("Su sueldo base + 0.35 es: ",nSueldo2)
