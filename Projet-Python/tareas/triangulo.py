n = int(input("¿Cuántas filas quieres? ")) #filas que quiere el usuario
x=1 #Fila actual que es el mismo número que el número de columnas que tiene que tener esa fila
y=1 #Número que hay que imprimir
z=1 #número de columnas que hay en la fila
frase = ''
for x in range(1,n+1):
   for z in range(1,x+1): #z recorre de 1 hasta x. Ejemplo en la 4 (x=4 z=1,2,3,4)
     frase+=(str(y)+(' '))
     y+=1
   print(frase)
   frase =''
