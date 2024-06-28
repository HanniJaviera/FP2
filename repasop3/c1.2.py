matriz_sencilla = [
[1, 2, 3],
[4, 5, 6]
]
print("imprimir matriz")
for elemento in matriz_sencilla:
	print(elemento)
print("imprimir un elemento por posición")
print(matriz_sencilla[1][0])
print("Imprimir todos los elementos")
for fila in matriz_sencilla:
	for elemento in fila:
		print(elemento, end=' ')
print() 

arreglo_3D = [
[
[1, 2, 3],
[4, 5, 6],
],
[
[7, 8, 9],
[10, 11, 12],
],
[
[13, 14, 15],
[16, 17, 18],
]
]
for capa in arreglo_3D:
 for fila in capa:
     for elemento in fila:
         print(elemento, end=' ')
     print()
 print()
