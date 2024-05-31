#Hacer un listado de compras

listado = { 
    'Frutas': {
        'Naranja': 1800,
        "Mora": 2000,
        "Pera": 1000
        },
    "Verdura": {
        "Espinaca": 3000,
        "Pimenton": 1000,
        "esparrago": 1500,
        "acelga": 2000
        },
    "Carne": {
        "pollo": 2000,
        "vacuno": 5000,
        "cerdo" : 7000
        }
    }
for key in listado:
    print(key,"", listado[key])

for key in listado:
    print(key, ":")
    for ll in listado[key]:
        print(ll, ":", listado[key][ll])

#precio de algo
    print ("pollo :",listado["Carne"]["pollo"])
