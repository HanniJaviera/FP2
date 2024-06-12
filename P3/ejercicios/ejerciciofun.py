lista= [1,2,3,4,5,6,7,8,9,10]
midiccionario ={'a': 1, 'b' : 2, 'c' : 3}


def recorridolista():
    for elemento in (lista):
     print (elemento)

recorridolista()


def buscarvalor (diccionario,key):
   if key in diccionario:
      return diccionario[key]
   else:
      return f"La clave '{key}' no existe en el diccionario."

clavebuscada = str(input("Ingrese numero indice: "))

resultado = buscarvalor (midiccionario, clavebuscada)
print (resultado)
      