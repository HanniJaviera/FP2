hotel = [
    [[],[],[],[],[],[],[],[]], #piso 1
    [[],[],[],[],[],[],[],[]], #piso 2
    [[],[],[],[],[],[],[],[]], #piso 3
    [[],[],[],[],[],[],[],[]], #piso 4
    [[],[],[],[],[],[],[],[]]  #piso 5
]
def reserva():
    print ("""Reserva de habitación
                   ¿En que piso desea reservar?""")
    piso = int (input())-1
    while True:
             if piso in (0,1,2,3,4):
                print ("Piso válido")
                break
             else:
                print ("""Piso incorrecto. 
                       Ingrese nuevamente el piso :""")
                piso = int (input())-1
    habitacion = int (input("Ingrese número de la habitación: "))-1
    while True:
             if habitacion in (0,1,2,3,4,5,6,7):
                print ("Habitación válida")
                break
             else:
                print ("""habitación incorrecto. 
                       Ingrese nuevamente el la habitación :""")
                habitacion = int (input())-1
    nombre = (input("Ingrese su nombre para reservar: "))
    while True:
             if nombre.isalpha():
                print ("""Nombre válido
                       ¡Reserva exitosa!""")
                break
             else:
                print ("""Nombre incorrecto. 
                       Ingrese nuevamente el nombre :""")
                nombre = (input())
    hotel [piso][habitacion]= nombre
    
def anular ():
    print ("Aquí puedes anular la habitación")
    piso = int (input("En que piso se encuentra la habitación :"))-1
    habitacion = int (input("número de la habitación: "))-1
    hotel [piso][habitacion] = []
    print ("Anulación exitosa")
    
def estadohabitacion():
    print ("Estado de la habitación")
    for i, piso in enumerate(hotel):
        for j, habitacion in enumerate(piso):
            estado = "reservado" if habitacion else "disponible"
            print (f"habitacion numero: {j+1} del piso {i+1} = {estado}")

def valor():
    valor = 0
    for i, piso in hotel:
        for j, habitacion in piso:
         if piso == 5:
            if not habitacion:
                valor = valor +0
            else:
                valor + valor + 100000
         else:
            if not habitacion:
                valor = valor + 0
            else:
                valor = valor + 20000
    print (valor) 
            

def info():
    print ("Información de habitaciones")
    print ("En que piso está la habitación")
    piso = int (input())-1
    print ("Número de la habitación")
    habitacion = int (input())-1
    print (f"Esta es la información de la habitación {habitacion}", hotel[piso][habitacion])

while True:
    print ("""
           ¡Bienvenido al hotel de la mejor ciudad LONDRES!
           ¿Qué deseas hacer?
           1. Reservar una habitación
           2. Anular reserva
           3. Buscar información de la habitación
           4. Buscar estado de la habitación
           5. Total ventas por día
           6. Guardar la información en un archivo txt
           7. Salir
           """)
    op = int (input("Ingrese la opción que desea realizar (1-7): ")) 
    match op:
        case 1:
            reserva()
        case 2:
            anular ()
        case 3:
            info()
        case 4:
           estadohabitacion()
        case 5:
            print ("Este es al total de venta por día")
            valor()
        case 6:
            with open ('hotel.txt', 'w') as archivo:
                for piso in range (5):
                    archivo.write (f"Piso {piso+1}\n")
                    for habitacion in range (8):
                        if habitacion == [] : 
                            estado = "disponible" 
                        else:
                            estado = "reservada"
                        archivo.write (f"habitacion {habitacion +1} : {estado}\n")
        case 7:
            print ("Gracias por venir")
            break
        case _:
            print ("Opción invalida")
                          
            
            
            