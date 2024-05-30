divisas = {"euro":"€", "Dolar":"$", "Yen":"¥"}
print("Que divisa quiere saber")
dato = str (input())
print (divisas.get(dato.title(), "La divisa no está"))