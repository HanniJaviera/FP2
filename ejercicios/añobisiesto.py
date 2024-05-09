print ("Escribe una año")
año = int (input())

if año %4 == 0: 
    if año% 100 !=0 or año%400 == 0:
      print ("Bisiesto")
    else:
      print ("No bisiesto")
