#Menu
estacionamiento = [[],[],[],[]]
print ("Bienvenido al Parking VIP")

while True:
    print ("¿Que desea hacer? Debes seleccionar del 1 al 5")
    print ("1.- Ingresar un vehículo")
    print ("2.- Listar vehículos")
    print ("3.- Borrar un vehículo")
    print ("4.- Conteo de vehículos")
    print ("5.- Salir")
    autoentrar = int (input())

    match autoentrar:
        case 1:
            print ("¿En que piso deseas aparcar?")
            piso = int (input())
            print ("Ingrese su patente")
            patente = str(input ())
            while len(patente) != 6:
                print ("Solo se permiten 6 digitos intente nuevamente")
                patente = str (input())
            estacionamiento[piso-1].append(patente)
            print (estacionamiento)
        case 2:
            print ("""
            Que listado deseas
            1- Listar todos
            2. Listar un piso específico
            3. Volver""")
            tipodelista = int (input())
            match tipodelista:
                case 1:
                    print ("Te nostraré el listado de todas las patentes del estacionamiento")
                    print (estacionamiento)
                case 2:
                    print ("¿Que piso deseas ver")
                    piso = int (input())
                    print ("Te mostrate la lista del piso: ",piso)
                    print (estacionamiento[piso-1])
                case 3: 
                    continue
        case 3:
            print ("Ingrese la patente del vehiculo que quiere eliminar")
            patente = str (input())
            estacionamiento.remove(patente)
        case 4:
            print ("""
            ¿Qué vehiculos quieres contar
            1.- Mostar cantidad de vehículos en total
            2.- Mostar cantidad de vehículos por piso
            3.- Mostar cantidad de vehículos de un piso
            4.- Volver """)
            tipo = int (input())
            match tipo:
                case 1: 
                    contador = 0
                    for elemento in range (4):    
                        contador=contador + len(estacionamiento[elemento])
                    print (contador)

                case 2:
                    for elemento in range (4):
                        print (len(estacionamiento[elemento]))
                case 3:
                    print ("Ingrese el piso que deseas saber")
                    piso = int (input())
                    print (len(estacionamiento[piso-1]))
                case 4:
                    continue
        case 5:
            break

                    

