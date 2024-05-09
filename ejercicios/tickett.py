print ("Ingrese su edad")
edad = int (input())
print ("Cuantos articulos compró?")
cantidad = int (input())

if edad >= 18 and cantidad >=2:
    print ("Si es mayor de edad y ha comprado más de un articulo")
elif edad >= 18 and cantidad <=1:
    print ("Es mayor de edad pero no cumple los requisistos ")
else:
    print ("Usted es menor de edad no cumple los requisitos")