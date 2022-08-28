'''
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas 
de una calculadora: sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python 
y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
'''
import time

hora = time.strftime('%H') 
minutos = time.strftime('%M') 

if int(hora) >= 19:
	print ("Es hora de irse a casa") 
else:
	print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))