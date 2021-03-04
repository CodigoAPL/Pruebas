import sqlite3

conexion = sqlite3.connect("Biblioteca")
cursor = conexion.cursor()

cursor.execute('''
    create table Biblioteca(
        ID integer primary key autoincrement,
        titulo varchar(50),
        categoria varchar(20),
        direccion varchar(60))               
    ''')

enlaces = [
    ("luiscarlos1", "filosofia", "https://www.youtube.com/watch?t=2180&v=Bb0txszJ5-E&feature=youtu.be"),
    ("luiscarlos2", "filosofia", "https://www.youtube.com/watch?v=8_WaEH26Caw"),
    ("luiscarlos3", "filosofia", "https://www.youtube.com/watch?v=ZBe94AtlDB4"),
    ("invariancia de lorentz", "fisica", "https://www.youtube.com/watch?list=PLAnA8FVrBl8AComQOG21MMOwveMRwbmsA&t=2107&v=-ivXJu_cFv0&feature=youtu.be"),
    ("titulo", "otro", "https://www.youtube.com/watch?v=ZBe94AtlDB4"),
    ("titulo", "otro", "https://www.youtube.com/watch?v=ZBe94AtlDB4"),
    ("titulo", "otro", "https://www.youtube.com/watch?v=ZBe94AtlDB4"),
    ("titulo", "otro", "https://www.youtube.com/watch?v=ZBe94AtlDB4"),
    ("articulo H.", "historia", "https://spainillustrated.blogspot.com/2011/10/antropologia-cultural-moderna-jose-acosta.html"),
    ("articulo c.", "ciencia", "https://evolucionyneurociencias.blogspot.com/2020/10/son-el-homicidio-y-el-suicidio.html"),
]

cursor.executemany("insert into Biblioteca values (null,?,?,?)", enlaces)

cursor.execute("select * from Biblioteca")
consulta = cursor.fetchall()
print(consulta)


cursor.execute("select * from Biblioteca")
consulta = cursor.fetchall()
direcciones = []
for i in range(len(consulta)):
    direcciones.append(consulta[i][3])
print(direcciones)

conexion.commit()
