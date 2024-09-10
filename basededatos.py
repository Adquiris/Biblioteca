import sqlite3

class BaseDeDatos:
    conexion = sqlite3.connect('HorizonteLiterario.db')
    cursorBD = conexion.cursor()

    def crearTablaLibros(self):
        self.cursorBD.execute('''
        CREATE TABLE IF NOT EXISTS LIBROS (
            ID_LIBRO INTEGER PRIMARY KEY AUTOINCREMENT,
            TITULO TEXT,
            GENERO TEXT,
            ANIO_PU INTEGER,
            DISPONIBLE BOOLEAN DEFAULT TRUE
        )''')

    def crearTablaUsuarios(self):
        self.cursorBD.execute('''
        CREATE TABLE IF NOT EXISTS USUARIOS (
            ID_USUARIO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE TEXT,
            CORREO TEXT,
            NUM_CONTACTO INTEGER
        )''')

    #---------------------------------------------------------------------------------------------------------------------------------#
    # CREATE
     
    def insertarLibro(self, titulo, genero, anio):
        self.cursorBD.execute('INSERT INTO LIBROS (titulo, genero, anio_pu) VALUES (?,?,?)', (titulo, genero, anio))
        self.conexion.commit()

    def insertarUsuario(self, nombre: str, correo: str, num_contacto: int):
        self.cursorBD.execute('INSERT INTO USUARIOS (nombre, correo, num_contacto) VALUES (?,?,?)', (nombre, correo, num_contacto))
        self.conexion.commit()

    #---------------------------------------------------------------------------------------------------------------------------------#
    # READ

    def imprimirTabla(self, tabla):
        self.cursorBD.execute(f'SELECT * FROM {tabla}')
        print(self.cursorBD.fetchall())

    def imprimirLibro(self, id):
        self.cursorBD.execute(f'SELECT * FROM LIBROS WHERE ID_LIBRO = {id}')
        print(self.cursorBD.fetchone())

    def imprimirUsuario(self, id):
        self.cursorBD.execute(f'SELECT * FROM USUARIOS WHERE ID_USUARIO = {id}')
        print(self.cursorBD.fetchone())

    #---------------------------------------------------------------------------------------------------------------------------------#
    # DELETE

    def eliminarRegistros(self, tabla):
        self.cursorBD.execute(f'DELETE FROM {tabla}')

    def eliminarLibro(self, id):
        self.cursorBD.execute(f'DELETE FROM LIBROS WHERE ID_LIBRO = {id}')
        print(f'\nLibro {id} eliminado')

    def eliminarUsuario(self, id):
        self.cursorBD.execute(f'DELETE FROM USUARIOS WHERE ID_USUARIO = {id}')
        print(f'\nUsuario {id} eliminado')
    
    #---------------------------------------------------------------------------------------------------------------------------------#
    # UPDATE

    def actualizarLibro(self, id: int, titulo: str, genero: str, anio: int, disponible: bool):
        self.cursorBD.execute(''' 
        UPDATE LIBROS
        SET TITULO = ?, ANIO_PU = ?, GENERO = ?, DISPONIBLE = 
        WHERE ID_LIBRO = ?
    ''', (titulo, anio, genero, disponible, id))
        

    def actualizarUsuario(self, id: int, nombre: str, correo: str, contacto: int):
        self.cursorBD.execute(''' 
        UPDATE USUARIOS
        SET NOMBRE = ?, CORREO = ?, NUM_CONTACTO = ?
        WHERE ID_USUARIO = ?
    ''', (nombre, correo, contacto, id))
