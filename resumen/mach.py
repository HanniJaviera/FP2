print ("--Bienvenido al sistema Python--")
print ("Seleccione una opción")
print ("1.- Opción 1")
print ("2.- Opción 2")
print ("3.- Opción 3")

opcion= int(input())

match opcion:
    case 1:
        print ("Usted ha elegido la opción 1")
    case 2:
        print ("Usted ha elegido la opción 2")
    case 3:
        print ("Usted ha elegido la opción 3")