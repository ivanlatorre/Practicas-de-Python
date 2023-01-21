"""
*Sintaxis en Python:

for variable in elemento iterable (lista, cadena, range, etc.):
// código Java y C#
for(i=0; i<10; i++){
    // hacer algo
}
"""
Lista = (100,10,200)
for x in Lista:# recorre una lista
    print(x)
print("-----------")


for x in range(10):#conteo
    print(x)

    print(*range(1, 11))
print("Range ")

for x in range(1,11):
    print (x, end="; ")
print("----- end -----")


