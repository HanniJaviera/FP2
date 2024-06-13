from defdicc import buscarvalor #agregar una funcion desde otro archivo solo la llamamos con from (nombre del archivo sin .py) y el import es la funcion que queremos llamar
def creadiccionario():
    dic_vacio={}
    while True:
     key=input("Ingrese una key")
     if key.lower()=="shazam":
      print(dic_vacio)
      break
     else:
      value=input("Ingrese el valor de la key anterior")
      dic_vacio[key] = value
    preg=input("ingrese la key a buscar")   
    print(buscarvalor(dic_vacio, preg))

creadiccionario()
