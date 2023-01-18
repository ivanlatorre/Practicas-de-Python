num1 = "120"
num2 = "150"
print(int(num1)+int(num2))
num3 = 103
sueldo = 1035.78
texto = "Curso de Aprendizaje"
print(num1)
print(num2)
print(num3)
print(sueldo)
print(texto)
print(type(texto))
print(type(num1))
print(type(num3))
#int (x) Convierte x datos a entero
#float (x) Convierte x en un número de punto flotante.
#str (x) Convierte x a una cadena.
# hex (x) Convierte x entero en una cadena hexadecimal.
print(num1+num2)#se concatenan
print(int(num1)+int(num2))#se suman string en su valor a numero entero
print(int(sueldo))#no considera el dato decimal
print("Sueldo Mensual: " ,sueldo) #no se esta convinando  error datos diferentes sin la coma
print("Sueldo Mensual: "+str(sueldo))#convierte el entero en string
print(float(num3))#entero a decimal
print(hex(num3))#hexadecimal a un entero
