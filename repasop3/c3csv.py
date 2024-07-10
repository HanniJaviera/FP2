import csv # permiso w es escritura
with open('datos.csv', 'w', newline='') as archivo_csv:
 escritor_csv = csv.writer(archivo_csv)
# Escribir una fila en el archivo CSV
 escritor_csv.writerow(['Nombre', 'Edad', 'Comuna'])
# Escribir múltiples filas en el archivo CSV
 escritor_csv.writerows([
 ['Esteban', 25, 'Santiago'],
 ['María', 30, 'Valparaíso'],
 ['Carlos', 22, 'Osorno'],
 ['Sigrid', 25, 'Santiago'],
 ['Daniela', 30, 'La Cisterna'],
 ['Aylen', 17, 'La florida']
 ])

# Leer Archivos CSV
import csv
# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# Modo común: 'r' (lectura)
with open('datos.csv', 'r', newline='') as archivo_csv:
 lector_csv = csv.reader(archivo_csv)
 for fila in lector_csv:
	 print(fila)

import csv
with open('datos.csv', 'r') as archivo_csv:
 lector_csv = csv.DictReader(archivo_csv)
# recorremos cada fila con un For
 for fila in lector_csv:
  nombre = fila['Nombre']
  edad = int(fila['Edad'])
  comuna = fila['Comuna']
  estado_edad = "Mayor de Edad" if edad >= 18 else "Menor de Edad"
  print(f"{nombre} tiene {edad} años, es {estado_edad} y vive en {comuna}")
