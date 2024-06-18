


while True:
 print ("""Qúe deseas hacer?
       1. Agregar acciones que realizaste en tu auto
       2. Ver la bitácora de acciones realizadas
       3. Guardar la bitácora
       4. Salir""")
 hacer = int(input())
 match hacer:
    case 1: print ("""
       ¿Qué acciones desea realizar en su auto
       1. Encender
       2. Activar alarma
       3. Estacionado
       4. Nivel de aceite bajo""")
accion = int (input())
 
