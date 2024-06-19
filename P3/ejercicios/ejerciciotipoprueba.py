import csv
from datetime import datetime
bitacora= []

def agregar_evento(evento):
 fecha_hora_actual = datetime.now().strftime("%d-%m-%Y %H-%M:%S")
 fecha_evento = f"{fecha_hora_actual}-{evento}"
 bitacora.append(fecha_evento)

 with open("bitacora.txt", mode='a' , newline='') as escri:
      escri.write("")
  


 while True:
  print ("""Qúe deseas hacer?
       1. Agregar acciones que realizaste en tu auto
       2. Ver la bitácora de acciones realizadas
       3. Guardar la bitácora
       4. Salir""")
  hacer = int(input())

  match hacer:
     case 1: 
       print ("""
        ¿Qué acciones desea realizar en su auto
        1. Encender
        2. Activar alarma
        3. Estacionado
        4. Nivel de aceite bajo 
        5. Volver al menú principal
              """) 
       accion = int (input()) 
     case 2: 
       print ("") 
