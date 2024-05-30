diccionario ={"nombre": "Cesar Huispe",
              "Fonos": [
                  91234565,
                  98765432],
              "email": "email@gmail.com",
              "activo":True}
print (diccionario)
for h in diccionario:
    valor=diccionario[h] #recorrer las listad por el nombre de las llaves que seria h
    print(h,valor)

print (diccionario["email"])

print("Que dato quiere saber: nombre, fono o email")
dato = str (input())
print (diccionario[dato])