cine = [
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]]
]


def valor ():
    if fila <= 2:
        print ("El valor del asiento es $10000")
    elif fila >= 3 and asiento <= 5:
        print ("El valor del asiento es $18500")
    else:
        print ("El valor del asiento es de $21500")

def total():
    total=0
    for i , fila in enumerate(cine):  
        for j , asiento in enumerate(fila):
            if fila == 0 or 1 or 2:
                if not asiento:
                 total = total+0
                else:
                    total = total +10000        
            elif fila == 3 or 4 or 5:
                if not asiento:
                 total = total+0
                else:
                    total = total +18500       
            else:
                if not asiento:
                 total = total+0
                else:
                    total = total + 21500
                    print (total) 
    print (total)
  

    
    
while True:

 print ("""
        Bienvenido a tu cine favorito
        Estas son las opciones que puedes realizar
        1. Reservar asientos
        2. Buscar información del asiento
        3. Ver estado de los asientos
        4. Totalizar ventas del día
        5. Guardar la información en un archivo txt
        6. Salir
        
        ¿Qué opción deseas realizar?
        """)
 op = int (input())
 match op:
    case 1:
        print ("En que fila desea ")
        fila = int (input())-1
        while True:
         if fila in (0,1,2,3,4,5,6,7,8,9):
            print ("Fila valida")
            break
         else:
            print ("Fila inválida, recuerde que tenemos de la fila del 1 al 10")
            print ("Ingrese nuevamente la fila")
            fila = int (input())-1
        print ("En que asiento desea ")
        asiento =int (input())-1
        while True:
         if asiento in (0,1,2,3,4,5,6,7,8,9):
            print ("Asiento valida")
            break
         else:
            print ("Asiento inválido, recuerde que tenemos del asiento del 1 al 10")
            print ("Ingrese nuevamente el asiento")
            asiento = int (input())-1
        print ("Nombre que desea agregar a su asiento")
        nombre = input()
        while True:
         if nombre.isalpha() :
            print ("Nombre valido")
            break
         else:
            print ("Datos erroneos, ingrese nuevamente solo letras")
            nombre = input ()
        valor()
        cine [fila][asiento]= nombre
    case 2:
        print ("¿Qué fila deseas buscar?")
        fila = int (input())-1
        print ("En que asiento deseas buscar ")
        asiento =int (input())-1
        print ("Esta es la información del asiento: nombre de la reserva: ", cine[fila][asiento])
    case 3:
        print ("Este es el estado de cada asiento")
        for i, fila in enumerate(cine):
              for j, lugar in enumerate(fila):
               estado = "reservado" if lugar else "disponible"
               print ("El asiento", j+1 , "fila", i+1 , ":", estado)
    case 4:
        print ("Este es el total de ventas del día")
        total()
    case 5:
        dato= ""
        with open ('micine.txt', 'w') as archivo:
            archivo.write (dato)
        with open ('micine.txt','r') as archivo:
             datos = archivo.read()
        print (dato)
    case 6:
        print ("Gracias por venir")
        break
    case _:
        print ("Opción invalida")
    
        
        
 