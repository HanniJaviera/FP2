#Validar si un ticket esta dentro del rango balido entre 100 y 750
#validar si va a cancha o galeria

print ("Ingrese su numero del ticket")
ticket = int (input())

if ticket >= 100 and ticket <= 750:
    print ("Acceso Permitido")
    if ticket >= 100 and ticket <=500:
        print ("Tienes acceso a cancha")
    if ticket >500 and ticket <=750:
         print ("Tienes acceso a galeria")
else:
    print ("Acceso Denegado")
