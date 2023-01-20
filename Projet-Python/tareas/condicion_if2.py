"""
Ingrese una edad:
* si la edad se encunetra entre 1 y 10 años
    que es un niño
* si la edad se encuentra entre 11 a 17 años
    que es un joven
* si la edad se encuentra mayor a 17 años
    que es un adulto
"""
nEdad = int(input("Ingrese su EDAD: "))

if nEdad >=1 and nEdad <=10:
    print("Que es un niño")
elif nEdad >=11 and nEdad <=17:
    print("Que es un joven")
else:
    print("que es un adulto")
print("Final del proceso")