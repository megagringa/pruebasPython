'''
Area triangulo por ingreso de teclado
'''
import math

base = float(input("Base:"))
altura = float(input("Altura:"))

def area_triangulo(base,altura):
    area = (base*altura)/2
    return area

area = area_triangulo(base,altura)

print(f"({base}*{altura})/2={area}")