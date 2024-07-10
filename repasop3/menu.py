
import csv

estacionamiento = [
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[]],
]

def compra(piso,lugar,patente):
    if piso == 0 or 1:
        print("este estacionamiento tiene un valor de 4500 por dia ")
        if not estacionamiento[piso][lugar]:
            estacionamiento[piso][lugar]=patente
    else :
        print("este lugar de estacionamiento tiene un valor de 2500 por dia ")
        if not estacionamiento[piso][lugar]:
            estacionamiento[piso][lugar]=patente  

def anular (piso,lugar):
    estacionamiento[piso][lugar]=[] 
    print("el lugar a sido desocupado ") 
    
def total():
    total = 0
    autos=0
    for i, piso in enumerate(estacionamiento):
        for j, lugar in enumerate(piso):
            if lugar:
                if i in [0, 1]:
                    total += 4500
                    autos +=1
                else:
                    total += 2500
                    autos +=1
    print(f"El total a cobrar por todos los autos estacionados es {total}")
def totalautos():
    autos=0
    for i, piso in enumerate(estacionamiento):
        for j, lugar in enumerate(piso):
            if lugar:
                if i in [0, 1]:
                    autos +=1
                else:
                    autos +=1
    print(f"El numero de espacios reservados es de {autos}")
    
while True:
    print ("""Bienvenido al estacionamiento
           ¿Qué deseas hacer?
           1.Ver espacio disponible del estacionamiento
           2.Reservar estacionamiento
           3.Anular estacionamiento
           4.Total de ingresos del día
           5. Mostrar el número total de espacios reservados
           6. Exportar a csv
           7. Salir""")
    op = int(input())
    match op :
        case 1: 
            print ("Esto son los espacios disponibles del estacionamiento")
            for i, piso in enumerate(estacionamiento):
              for j, lugar in enumerate(piso):
               estado = "ocupado" if lugar else "no ocupado"
               print(f"El lugar {j+1} del piso {i+1} se encuentra {estado}")
        case 2:
            print ("Que piso y estacionamiendo deseas reservar (piso 1-8, estacionamiento 1-10)")
            piso= int (input())-1
            lugar = int (input()) -1
            print ("Ingrese su patente")
            patente= input()
            compra (piso,lugar,patente)
        case 3:
            print ("Anular")
            print ("En que piso te alojaste")
            piso = int (input())-1
            print ("en que lugar")
            lugar = int(input())-1
            anular (piso,lugar)
        case 4:
            total()
        case 5:
            totalautos()
        case 6: 
            with open('estacionamiento.csv','w', newline='') as archivo_csv:
                writer = csv.writer(archivo_csv)
                writer.writerow(["Piso", "Lugar", "Patente"])
                for i, piso in enumerate(estacionamiento):
                  for j, lugar in enumerate(piso):
                    patente = lugar if lugar else "Vacío"
                    writer.writerow([i + 1, j + 1, patente])
            print(f"La información ha sido exportada a {archivo_csv}.")
        case 7:
            break