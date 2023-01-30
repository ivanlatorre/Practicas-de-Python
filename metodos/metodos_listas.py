lista = list(["hola","Iván",30,56,25,True])
resultado = len(lista)
#cantidad de elementos de la lista
print("lista",resultado)
#agregando con append
lista.append("JAJAJAJA")
print("agregando con append: ", lista)
#agregando un elemento en la lista  en un indice especifico
lista.insert(2,"TOMAAAAA")
print("agregando al indice 2: ",lista)
#agregando otra lista con extend
lista.extend([False,2030])
print("agregando otra lista con extend: ",lista)
#eliminando un elemento de la lista por su indice POP
print("antes del pop: ",len(lista))
lista.pop(0)#primer elemento de la lista
print("despues del pop: ",len(lista))
print("lista: ",lista)
lista.pop(-1)#ultimo elemento de la lista
print("pop con -1(ultimo elemento de la lista)",lista)
#remove elimina elemento por su valor
lista.remove("TOMAAAAA")#si no encuentra el elemento indicado da error
print("lista despues de remove: ",lista)

#eliminando todos los elementos de toda la lista
lista.clear()
(print("lista despues del clear: ",lista))
lista_nueva = list([34,56,23,True, False,True])
print("lista nueva sin cadenas de texto: ",lista_nueva)
#sort oderna las lista sin cadenas de texto boleanos primeros y despues numeros
#para ordenar la lista en orden ascendente
lista_nueva.sort()
print("lista nueva con sort: ",lista_nueva)
lista_nueva.sort(reverse=True)
print("lista nueva con sort reverse: ",lista_nueva)
#invirtiendo los elementos de  una lista
lista_nueva.reverse()
print("lista nueva con metodo reverse",lista_nueva)
prueba = [34,56,23, True, False,False]
print("lista prueba: ",prueba)
prueba.sort()
print("lista sin list con sort: ",prueba)
#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista_nueva.index(56)
print("Elemento encontrado en lista nueva",elemento_encontrado)
#lista de conjuntos
print("elementos en el set (conjutos): ",dir(set(["valo1","valor2"])))



