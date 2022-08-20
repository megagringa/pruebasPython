'''
Escribe una función que calcule el área de un triángulo, 
recibiendo la altura y la base como parámetros y 
otra función que calcule el área de un círculo recibiendo el radio del mismo.
'''
import math

def area_triangulo(altura: float, base: float) -> float:
    return ((altura*base)/2)

def area_circulo(radio: float) -> float:
    return (math.pi*(radio**2))

print(f"Área de triangulo: {area_triangulo(2,2)}")
print(f"Área del círculo: {area_circulo(4)}")
    
