'''
Peso del usuario
Altura del usuario
Calcular masa corporal imc
'''

peso = input("¿Escriba su peso en kg? ")  
estatura = input("¿Escriba su estatura en metros?")  
imc = round(float(peso)/float(estatura)**2,2) 
print("Tu masa corporal es " + str(imc))