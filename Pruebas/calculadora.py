'''
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: 
sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python 
y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
'''

from __future__ import division
import metodoscalculadora as cl

suma = cl.sumar(2,4)
resta = cl.restar(4,1)
multiplicacion = cl.multiplicar(4,12)
division01 = cl.dividir(12,3)
division02 = cl.dividir(3,0)

print("Resultados:")
print(f"La suma es {suma}")
print(f"La resta es {resta}")
print(f"La multiplicacion es {multiplicacion}")
print(f"La division es {division01}")
print(f"La division es {division02}")