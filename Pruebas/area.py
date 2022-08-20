'''
Escribe una función que calcule el área de un triángulo, 
recibiendo la altura y la base como parámetros y 
otra función que calcule el área de un círculo recibiendo el radio del mismo.
'''
base = input("Base:")
altura = input("Altura:")


def area_triangulo(base,altura):
    return (base*altura)/2
    

print(area_triangulo(base,altura))

    
