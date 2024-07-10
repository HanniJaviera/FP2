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
    for i , piso in enumerate(estacionamiento):
        total=0
        for j , lugar in enumerate(piso):
            if piso == 0 or 1:
                if not lugar:
                 print(f"en el lugar {j+1} del piso {i+1} no se encuentra ocupado ")
                else:
                    total = total +4500
                    print (total)
                
            else:
                if not lugar:
                 print(f"en el lugar {j+1} del piso {i+1} no se encuentra ocupado ")
                else:
                    total = total + 2500
                    print(total)    
    
while True:
    print ("""Bienvenido al estacionamiento
           ¿Qué deseas hacer?
           1.Ver espacio disponible del estacionamiento
           2.Reservar estacionamiento
           3.Anular estacionamiento
           4.Total de ingresos del día
           5. Mostrar el número total de espacios reservados
           6. Salir""")
    op = int(input())
    match op :
        case 1: 
            print ("Esto son los espacios disponibles del estacionamiento")
            for elemento in estacionamiento:
                 print (elemento) 
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
            print ("Este es el total de ingresos por día")
            total()
        case 5:
            def exportar_a_csv(estacionamiento, filename="estacionamiento.csv"):
                 with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Piso", "Lugar", "Patente"])
                    for i, piso in enumerate(estacionamiento):
                        for j, lugar in enumerate(piso):
                            patente = lugar if lugar else "Vacío"
                            writer.writerow([i + 1, j + 1, patente])
                 print(f"La información ha sido exportada a {filename}.")
                 
                 print ("Gracias por venir")
            with open('estacionamiento.csv', 'w', newline='') as estacionamiento_csv:
                 escritor_csv = csv.writer(estacionamiento_csv)
                 escritor_csv.writerow(['Piso', 'Lugar', 'Patente'],)
                 for elemento, piso in enumerate(estacionamiento):
                     for i, lugar in enumerate(piso): 
                         if patente==lugar:
                             print(lugar) 
                         else: 
                            print ("vacio")  
        case 6:
            print ("Gracias por venir")  
            break