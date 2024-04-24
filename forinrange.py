# Escribir un programa que pida al usuario un número entero positivo y 
#muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
n = int(input("Introduce un número entero positivo: "))
for i in range(2, n+1, 2): #obligatorio es el primero que va hacer si o si, y es el limite inferior y el segundo el limite superior
    print(i, end=", ") #end hace que los numeros vayan para el lado en vez de hacia abajo

