
stay=True
while stay:
 print ("--Bienvenido al sistema Python--")
 print ("Seleccione una opción")
 print ("1.- Opción 1")
 print ("2.- Opción 2")
 print ("3.- Opción 3")
 print ("4.- Salir")

 opcion= int(input())

 match opcion:
     case 1:
        print ("Usted ha elegido la opción 1")
     case 2:
        print ("Usted ha elegido la opción 2")
     case 3:
        print ("Usted ha elegido la opción 3")
     case 4:
        stay=False
        print ("Gracias por venir") 
     case _: # el "_" significa cualquier numero que no define
        print ("menu invalido")