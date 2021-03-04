import webbrowser
import sqlite3


def llamar(url):
    webbrowser.open_new(url)


def pulsar(boton, texto, nueva_direccion):
    texto.bind("<Button-1>", lambda e: llamar(nueva_direccion))
    reemplazar_direccion(int(boton.cget("text")[20:]), nueva_direccion)


def reemplazar_direccion(n_linea, nueva_direccion):
    conexion = sqlite3.connect("Biblioteca")
    cursor = conexion.cursor()
    cursor.execute("update Biblioteca set direccion = ? where ID = ?", (nueva_direccion, n_linea))
    conexion.commit()
    conexion.close()


def obtener_direcciones():
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
