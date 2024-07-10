#crear archivo, w es permiso de escritura
#Las comillas al inicio y 3 al final del texto representan un texto
#con saltos de línea
datos = """Este es un archivo de texto simple que no tiene 
ningún formato en particular, lo podemos utilizar
para guardar todo tipo de texto. 
"""
with open('archivo.txt', 'w') as archivo:
	archivo.write(datos)

with open('archivo.txt', 'r') as archivo:
	datos = archivo.read()
print(datos)
