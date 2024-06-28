def perimetro(num1,num2): #se definio la def en dos argumentos -> es num1 y num2
  result=num1*2+num2*2
  return result
def area(num1,num2): #se definio la def en dos argumentos -> es num1 y num2
  result=num1*num2
  return result

print ("ingrese el lado 1")
num1=int (input())
print ("Ingrese el ancho 2")
num2=int (input())
print (area(num1,num2)) #sale el resultado que seria la suma, el usuario aqui de el argumento de la funcion
print (perimetro(num1,num2))