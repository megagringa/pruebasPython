'''
Tomar un dato por teclado, que no sea menor a 20, ni un mayor a 100
Tomar el dato y pasarlo a la variable numero,
En caso de ser menor a 20 avisar,
En caso de ser mayor a 500 avisar,
En caso de estar en el medio avisar.
'''

minimo = 20
maximo = 100
dato = input()
numero = int(dato)

if (numero < minimo):
    print("Valor bajo")
    
if (numero > maximo):
    print("Valor alto")
    
if (numero > minimo) and (numero < maximo):
    print("Valor medio")