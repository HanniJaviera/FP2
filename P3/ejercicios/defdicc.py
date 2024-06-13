
def buscarvalor (diccionario,key):
   if key in diccionario:
      return diccionario[key]
   else:
      return f"La clave '{key}' no existe en el diccionario."