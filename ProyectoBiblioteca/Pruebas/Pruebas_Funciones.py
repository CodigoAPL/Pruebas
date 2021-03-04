import webbrowser
from io import open
import sqlite3


def llamar(url):
    webbrowser.open_new(url)


def pulsar(boton, texto, nueva_dirección):
    texto.bind("<Button-1>", lambda e: llamar(nueva_dirección))
    Reemplazar_dirección(int(boton.cget("text")[20:]), nueva_dirección)


def Reemplazar_dirección(n_linea, nueva_dirección):
    conexion = sqlite3.connect("Biblioteca")
    cursor = conexion.cursor()
    cursor.execute("update Biblioteca set direccion = ? where ID = ?", (nueva_dirección, n_linea))
    conexion.commit()
    conexion.close()


def Obtener_direcciónes():
    conexion = sqlite3.connect("Biblioteca")
    cursor = conexion.cursor()

    cursor.execute("select * from Biblioteca")
    consulta = cursor.fetchall()
    direcciones = []
    for i in range(len(consulta)):
        direcciones.append(consulta[i][3])

    conexion.commit()
    conexion.close()
    return direcciones
