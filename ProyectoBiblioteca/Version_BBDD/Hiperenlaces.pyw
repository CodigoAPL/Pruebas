from tkinter import *
from Funciones import *


url = obtener_direcciones()

ventana = Tk()
ventana.title("Bibliotéca")
marco = Frame(ventana)


# Etiquetas de texto:

e1 = Label(marco, text="Video 1", fg="blue", cursor="hand2", padx=10, pady=20)
e1.bind("<Button-1>", lambda e: llamar(url[0]))
e1.grid(row=1, column=1)
e2 = Label(marco, text="Video 2", fg="blue", cursor="hand2", padx=10, pady=20)
e2.bind("<Button-1>", lambda e: llamar(url[1]))
e2.grid(row=2, column=1)
e3 = Label(marco, text="Video 3", fg="blue", cursor="hand2", padx=10, pady=20)
e3.bind("<Button-1>", lambda e: llamar(url[2]))
e3.grid(row=3, column=1)
e4 = Label(marco, text="Video 4", fg="blue", cursor="hand2", padx=10, pady=20)
e4.bind("<Button-1>", lambda e: llamar(url[3]))
e4.grid(row=4, column=1)
e5 = Label(marco, text="Video 5", fg="blue", cursor="hand2", padx=10, pady=20)
e5.bind("<Button-1>", lambda e: llamar(url[4]))
e5.grid(row=5, column=1)
e6 = Label(marco, text="Video 6", fg="blue", cursor="hand2", padx=10, pady=20)
e6.bind("<Button-1>", lambda e: llamar(url[5]))
e6.grid(row=6, column=1)
e7 = Label(marco, text="Video 7", fg="blue", cursor="hand2", padx=10, pady=20)
e7.bind("<Button-1>", lambda e: llamar(url[6]))
e7.grid(row=7, column=1)
e8 = Label(marco, text="Video 8", fg="blue", cursor="hand2", padx=10, pady=20)
e8.bind("<Button-1>", lambda e: llamar(url[7]))
e8.grid(row=8, column=1)
e9 = Label(marco, text="Artículo H.", fg="blue", cursor="hand2", padx=10, pady=20)
e9.bind("<Button-1>", lambda e: llamar(url[8]))
e9.grid(row=9, column=1)
e10 = Label(marco, text="Artículo C.", fg="blue", cursor="hand2", padx=10, pady=20)
e10.bind("<Button-1>", lambda e: llamar(url[9]))
e10.grid(row=10, column=1)


# Entradas de texto:

d1 = Entry(marco)
d1.grid(row=1, column=2, padx=10, pady=20)
d2 = Entry(marco)
d2.grid(row=2, column=2, padx=10, pady=20)
d3 = Entry(marco)
d3.grid(row=3, column=2, padx=10, pady=20)
d4 = Entry(marco)
d4.grid(row=4, column=2, padx=10, pady=20)
d5 = Entry(marco)
d5.grid(row=5, column=2, padx=10, pady=20)
d6 = Entry(marco)
d6.grid(row=6, column=2, padx=10, pady=20)
d7 = Entry(marco)
d7.grid(row=7, column=2, padx=10, pady=20)
d8 = Entry(marco)
d8.grid(row=8, column=2, padx=10, pady=20)
d9 = Entry(marco)
d9.grid(row=9, column=2, padx=10, pady=20)
d10 = Entry(marco)
d10.grid(row=10, column=2, padx=10, pady=20)


# Botones:

b1 = Button(marco, text="establecer enlace nº1", command=lambda: pulsar(b1, e1, d1.get()), padx=10, pady=0)
b1.grid(row=1, column=3)
b2 = Button(marco, text="establecer enlace nº2", command=lambda: pulsar(b2, e2, d2.get()), padx=10, pady=0)
b2.grid(row=2, column=3)
b3 = Button(marco, text="establecer enlace nº3", command=lambda: pulsar(b3, e3, d3.get()), padx=10, pady=0)
b3.grid(row=3, column=3)
b4 = Button(marco, text="establecer enlace nº4", command=lambda: pulsar(b4, e4, d4.get()), padx=10, pady=0)
b4.grid(row=4, column=3)
b5 = Button(marco, text="establecer enlace nº5", command=lambda: pulsar(b5, e5, d5.get()), padx=10, pady=0)
b5.grid(row=5, column=3)
b6 = Button(marco, text="establecer enlace nº6", command=lambda: pulsar(b6, e6, d6.get()), padx=10, pady=0)
b6.grid(row=6, column=3)
b7 = Button(marco, text="establecer enlace nº7", command=lambda: pulsar(b7, e7, d7.get()), padx=10, pady=0)
b7.grid(row=7, column=3)
b8 = Button(marco, text="establecer enlace nº8", command=lambda: pulsar(b8, e8, d8.get()), padx=10, pady=0)
b8.grid(row=8, column=3)
b9 = Button(marco, text="establecer enlace nº9", command=lambda: pulsar(b9, e9, d9.get()), padx=10, pady=0)
b9.grid(row=9, column=3)
b10 = Button(marco, text="establecer enlace nº10", command=lambda: pulsar(b10, e10, d10.get()), padx=10, pady=0)
b10.grid(row=10, column=3)

marco.pack()

ventana.mainloop()
