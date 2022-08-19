'''
Crear nota1 = 6
Crear nota2 = 4
Crear nota3 = 7
Crear nota_media que tenga el valor medio de las 3 notas anteriores
crear nota_finalque tenga el valor aprobado (mayor o iguala 5)
'''

nota1 = 6
nota2 = 4
nota3 = 7
nota_media = (nota1 + nota2 + nota3)/3
if(nota_media>=5):
    nota_final = "aprobado"

    print("nota del señor")
    print("",nota1,"",nota2,"",nota3)
    print("Su promedio es ",nota_media)
    print(nota_final)
