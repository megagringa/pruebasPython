'''
En este segundo ejercicio, 
tendréis que crear un programa que tenga una clase llamada Alumno 
que tenga como atributos su nombre y su nota. 
Deberéis de definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
'''
class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 
    def resultado(self):
            if self.nota < 5:
                print("El alumno ha suspendido")
            else:
                print("El alumno ha aprobado")
 

alumno1=Alumno()
alumno2=Alumno()

alumno1.inicializar("María",8)
alumno2.inicializar("Pepe",4)
 
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()