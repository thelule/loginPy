import sqlite3

def insertar():
    conexion = sqlite3.connect('libros.db')

    print("Estás en la función insertar")

    nombre1=input("Escribe el título: ")
    autor1=input("Escribe el autor: ")
    anio1=input("Escribe el año: ")

    consulta = conexion.cursor()

    strConsulta = "insert into libros(nombre, autor, anio) values ('" + nombre1 + "','" + autor1 + "','" + anio1 + "')"

    print(strConsulta)
    consulta.execute(strConsulta)
    consulta.close()
    conexion.commit()
    conexion.close()

insertar()
