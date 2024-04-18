ticket_valido=False

folio_valido=123

print ("Ingrese el numero del folio")
n_folio=int(input())

if n_folio== folio_valido:
    ticket_valido=True
if ticket_valido: 
    print ("Este ticket es valido")
else:
    print ("Este ticket es invalido")