stay=True
gasto=0
nombre=""
edad=0
while stay:
 print ("--Bienvenido al sistema Python--")
 print ("Seleccione una opción")
 print ("1.- Escriba su nombre")
 print ("2.- cuanto gaste")
 print ("3.- Ingrese su año de nacimiento")
 print ("4.- mis gastos")
 print ("5.- Salir")

 opcion= int(input())

 match opcion:
     case 1:
        nombre=input()
        print ("este es tu nombre " + nombre)
     case 2:
        gasto= gasto + int (input())
     case 3:
        edad = int (input())
     case 4:
        print ("Hola ",nombre, "su edad es ", edad, "el total de sus gastos es" ,gasto )
     case 5:
        stay=False
        print ("Gracias por venir") 
     case _: # el "_" significa cualquier numero que no define
        print ("menu invalido")