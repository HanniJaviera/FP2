lista = [41,62,73,4,35]
lista.append(lista[2]+lista[4]) 
lista.append(lista[0]+lista[1]) #añade elemento a lista


for elemento in lista:
    print (elemento)

import random #se importa la clase random
lista = [1,2,3,4,5]
num=random.randint(0,100) #te da un numero aleatorio del 0 al 100
lista.append(num)

for elemento in lista:
    print (elemento)