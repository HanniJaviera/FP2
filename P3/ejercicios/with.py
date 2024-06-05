
from datetime import datetime
now=datetime.now()
tiempo=now.strftime("%Y%m%d_%H%M%S")


num =0
lista= "Los autos en el parking son", str(num)

with open(f'listaN_javi.txt{tiempo}', 'w') as archivo:
    archivo.write(str(lista))

