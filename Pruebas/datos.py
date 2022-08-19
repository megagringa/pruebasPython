'''
Para este ejercicio tenéis que crear en la consola de 
python variables que representen los siguientes datos de un contacto:
Nombre
Apellidos
Edad
Email
Teléfono
Casado (verdadero o falso)
Con Hijos (verdadero o falso)
Lista de amigos
Películas vistas (diccionario con clave y valor. El valor será el título de la película)
Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
'''
nombre = "Juan Pablo"
apellido = "Lopez"
edad = 33
email = 'nolodigo@gmail.com'
telefono = 12345
esposa = 1
if (esposa):
    casado = "verdadero"
hijo = 1
if(hijo>=1):
    hijo= "verdadero"

amigos = ["vierja", "etc" ]
peliculas = {"Batman": 1, "Spiderman":2}

print(nombre)
print(apellido)
print(edad)
print(email)
print(telefono)
print(casado)
print(hijo)
print(amigos)
print(peliculas)