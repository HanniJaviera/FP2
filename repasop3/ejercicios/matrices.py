cine = [
    [[],[],[]],
    [[],[],[]]
]


print ("En que asiento desea comprar")
for elemento in cine:
    print (elemento)
print ("en que fila")
fila = int (input()) -1
print ("en que asiento")
asiento = int (input()) -1
print ("ingrese su nommbre")
nombre = input()
cine[fila][asiento] = nombre
for elemento in cine:
    print (elemento)
    
print ("Qué fila deseas ver la información")
fila1 = int (input())-1
print ("Qué asiento deseas ver la información")
asiento1 = int (input())-1
print (cine[fila1][asiento1])
if asiento == []:
    print ("Este asiento está vacío")
else:
    print ("Este asiento está ocupado")

#crear archivo csv

import csv

with open ('cine.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer (archivo_csv)
    escritor_csv.writerow (['fila', 'Asiento', 'Nombre'],)
    for i,lugar in enumerate(cine):
        for j,asiento in enumerate(lugar):
           nombre = asiento if asiento else "Vacío"
           escritor_csv.writerow([i + 1, j + 1, nombre])
    print(f"La información ha sido exportada a {archivo_csv}.")

# crear archivo json

import json

with open ('archivo.json', 'w') as archivo:
    json.dump (cine, archivo)
    
with open ('archivo.json', 'r') as archivo:
    datos_leidos = json.load (archivo)
    print (datos_leidos)
    
#crear archivo txt

datos = """texto"""
with open ('cine.txt', 'w') as archivo.txt:
    archivo.write (datos)
with open ('cine.txt', 'r') as archivo.txt:
    datos = archivo.read()
print (datos)