milista = [1,2,3,4,5]

for elemento in milista:
    print (elemento)
    
print (milista[2])

milista.append (8) #agregar elementos a la lista

for elemento in milista:
    print (elemento)
    
milista.insert (3, "Juan")

for elemento in milista:
    print (elemento)
    
milista.remove("Juan")
for elemento in milista:
    print (elemento)
    
milista.reverse()

for elemento in milista:
    print (elemento)

milista = [ 1,5,3,6,2,4] 
milista.sort()

for elemento in milista:
    print(elemento)