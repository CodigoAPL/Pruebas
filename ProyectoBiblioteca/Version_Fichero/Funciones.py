import webbrowser
from io import open


def llamar(url):
    webbrowser.open_new(url)


def pulsar(boton, texto, nueva_dirección):
    texto.bind("<Button-1>", lambda e: llamar(nueva_dirección))
    Reemplazar_dirección(int(boton.cget("text")[20:]), nueva_dirección)


def Reemplazar_dirección(n_linea, nueva_dirección):
    fichero = open("Enlaces.txt", "r")
    contenido = fichero.readlines()
    contenido[n_linea - 1] = nueva_dirección + "\n"
    fichero.close()

    fichero = open("Enlaces.txt", "w")
    fichero.writelines(contenido)
    fichero.close()


def Obtener_direcciónes():
    direcciones = []
    fichero = open("Enlaces.txt", "r")
    contenido = fichero.readlines()
    for i in range(len(contenido)):
        direcciones.append(contenido[i])
    return direcciones
