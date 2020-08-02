import sqlite3

conexion = sqlite3.connect('libros.db')
consulta = conexion.cursor()

tabla = "CREATE TABLE libros (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
    "nombre VARCHAR(30) NOT NULL,"\
    "autor VARCHAR(30) NOT NULL,"\
    "anio INTEGER(9) NOT NULL);"

print(tabla)

if (consulta.execute(tabla)):
    print("La tabla se creó")
else:
    print("La tabla no se creó")

consulta.close()
conexion.commit()
conexion.close()