def validarfolio():
 ticket_valido=False
 folio_valido=123
 print ("Ingrese el numero de folio")
 n_folio=int (input())

 if n_folio==folio_valido:
    ticket_valido=True

def suma(num1,num2): #se definio la def en dos argumentos -> es num1 y num2
  result=num1+num2
  return result

print ("Ingrese 2 numeros")
num1=int (input())
num2=int (input())
print (suma(num1,num2)) #sale el resultado que seria la suma, el usuario aqui de el argumento de la funcion