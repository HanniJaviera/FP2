print("Ingrese su inversión")
inversion= int (input())
print("Ingrese el interes")
interes=int (input())
print ("Ingrese la cantidad de año")
año=int (input())

for i in range (año):
    inversion *= 1 + interes/100
    print ("La inversion al año" + str(i+1) + "años:" + str(round(inversion, 2)))
 

