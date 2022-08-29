'''
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
la columna id de tipo entero, 
la columna nombre que será de tipo texto 
y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, 
como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
'''

import sqlite3

db_connection = sqlite3.connect('ej1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Maria', 'Lopez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Pepe', 'Rodriguez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Maria', 'Martinez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Francisco', 'Perez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Jorge', 'Herrero')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Clara', 'García')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Monica', 'Santamaria')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Pablo', 'Villanueva')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Maria'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()