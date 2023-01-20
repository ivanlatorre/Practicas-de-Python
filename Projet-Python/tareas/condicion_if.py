#https://www.youtube.com/@VictorRamosDatSoft/playlists
"""
if condición:
        aqui van las órdenes que se ejecutan si la condición es
        cierta y que pueden ocupar varias líneas
"""
"""nEdad = int(input("Ingrese su edad: "))
if nEdad>=18:
    print("Tu eres mayor de edad")#respetar el espacio bajo condición if
else:
    print("Eres menor de edad")"""
nEdad = int(input("Ingrese su edad: "))
if nEdad<18:
    print("Eres menor de edad")
elif nEdad==18:
    print("Tu edad es 18 años")
else:
    print("Eres mayor de edad")

