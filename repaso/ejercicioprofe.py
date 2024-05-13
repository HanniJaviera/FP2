#Estudiantes, les mando una tarea para practicar que incluye todo lo visto hasta ahora

#Crear un programa que pueda hacer lo siguiente

#Ingresar nombre de alumno
#Ingresar carrera 1 2 3
#la carrera 1 dura 8 semestres
#la carrera 2 dura 10 semestres
#la carrera 3 dura 6 semestres
#Basado en la información anterior calcular
#Calcular el total por año
#Calcular el valor total por carrera
#Consideraciones
#El valor mensual es de 300.000
#Si la carrera dura más de 6 semestres, tiene descuento de 15%
#Cada semestre consta de 5 meses
#Es de carácter opcional, pero les sirve para practicar.
valormes = 300000

nombre = input ("Ingrese su nombre: ")
carrera = input ("Ingrese numero de carrera (1-3)")
if carrera == "1":
    print ("Su carrera dura 8 semestres")
    valoraño = valormes*2
    valorcarrera= valoraño*4
    print("Estimada:", nombre)
    print ("El valor de la carrera es $", valorcarrera, " y por año es: ", valoraño)
    valordescuento= valorcarrera*0.75
    print ("Pero obtiene un 15% de dscto y le queda el valor de la carrera total en $",valordescuento)
elif carrera == "2":
    print ("Su carrera dura 10 semestres")
    valoraño = valormes*2
    valorcarrera= valoraño*5
    print("Estimada:", nombre)
    print ("El valor de la carrera es $", valorcarrera, " y por año es: ", valoraño)
    valordescuento= valorcarrera*0.75
    print ("Pero obtiene un 15% de dscto y le queda el valor de la carrera total en $",valordescuento)
elif carrera =="3":
    print("Estimada:", nombre)
    print ("Su carrera dura 6 semestres")
    valoraño = valormes*2
    valorcarrera= valoraño*3
    print ("El valor de la carrera es $", valorcarrera, " y por año es: ", valoraño)
else:
    print ("No existe su carrera")