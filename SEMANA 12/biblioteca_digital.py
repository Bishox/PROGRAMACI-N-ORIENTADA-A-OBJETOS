import sqlite3

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"


class Biblioteca:
    def __init__(self):
        self.db_name = 'biblioteca.db'
        self.crear_tablas()

    def crear_tablas(self):
        """Crea las tablas necesarias en la base de datos."""
        conexion = sqlite3.connect(self.db_name)
        cursor = conexion.cursor()
        
        # Crear tabla de libros
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            categoria TEXT NOT NULL
        )
        ''')
        
        # Crear tabla de usuarios
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario TEXT PRIMARY KEY,
            nombre TEXT NOT NULL
        )
        ''')
        
        # Crear tabla de libros prestados
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros_prestados (
            id_usuario TEXT,
            isbn TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
            FOREIGN KEY (isbn) REFERENCES libros (isbn),
            PRIMARY KEY (id_usuario, isbn)
        )
        ''')
        
        conexion.commit()
        conexion.close()

    def ejecutar_query(self, query, params=()):
        """Ejecuta una consulta SQL que modifica la base de datos."""
        conexion = sqlite3.connect(self.db_name)
        cursor = conexion.cursor()
        cursor.execute(query, params)
        conexion.commit()
        conexion.close()

    def consultar_query(self, query, params=()):
        """Consulta la base de datos y devuelve resultados."""
        conexion = sqlite3.connect(self.db_name)
        cursor = conexion.cursor()
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        conexion.close()
        return resultados

    def añadir_libro(self, libro):
        """Añadir un libro a la biblioteca."""
        query = 'INSERT INTO libros (isbn, titulo, autor, categoria) VALUES (?, ?, ?, ?)'
        params = (libro.isbn, libro.titulo, libro.autor, libro.categoria)
        try:
            self.ejecutar_query(query, params)
            print(f"Libro añadido: {libro}")
        except sqlite3.IntegrityError:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        """Quitar un libro de la biblioteca."""
        query = 'DELETE FROM libros WHERE isbn = ?'
        self.ejecutar_query(query, (isbn,))
        print(f"Libro con ISBN {isbn} ha sido quitado de la biblioteca.")

    def registrar_usuario(self, nombre, id_usuario):
        """Registrar un nuevo usuario."""
        query = 'INSERT INTO usuarios (id_usuario, nombre) VALUES (?, ?)'
        params = (id_usuario, nombre)
        try:
            self.ejecutar_query(query, params)
            print(f"Usuario registrado: {nombre}")
        except sqlite3.IntegrityError:
            print(f"El ID de usuario {id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        """Eliminar un usuario de la biblioteca."""
        query = 'DELETE FROM usuarios WHERE id_usuario = ?'
        self.ejecutar_query(query, (id_usuario,))
        print(f"Usuario con ID {id_usuario} ha sido eliminado.")

    def prestar_libro(self, isbn, id_usuario):
        """Prestar un libro a un usuario."""
        query = 'SELECT 1 FROM libros WHERE isbn = ?'
        if not self.consultar_query(query, (isbn,)):
            print(f"El libro con ISBN {isbn} no está disponible.")
            return

        query = 'SELECT 1 FROM usuarios WHERE id_usuario = ?'
        if not self.consultar_query(query, (id_usuario,)):
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        query = 'INSERT INTO libros_prestados (id_usuario, isbn) VALUES (?, ?)'
        params = (id_usuario, isbn)
        try:
            self.ejecutar_query(query, params)
            print(f"Libro con ISBN {isbn} prestado al usuario {id_usuario}.")
        except sqlite3.IntegrityError:
            print(f"El usuario con ID {id_usuario} ya tiene prestado el libro con ISBN {isbn}.")

    def devolver_libro(self, isbn, id_usuario):
        """Devolver un libro prestado por un usuario."""
        query = 'DELETE FROM libros_prestados WHERE id_usuario = ? AND isbn = ?'
        self.ejecutar_query(query, (id_usuario, isbn))
        print(f"Libro con ISBN {isbn} devuelto por el usuario {id_usuario}.")

    def buscar_libros(self, titulo=None, autor=None, categoria=None):
        """Buscar libros por título, autor o categoría."""
        query = 'SELECT * FROM libros WHERE 1=1'
        params = []

        if titulo:
            query += ' AND titulo = ?'
            params.append(titulo)
        if autor:
            query += ' AND autor = ?'
            params.append(autor)
        if categoria:
            query += ' AND categoria = ?'
            params.append(categoria)
        
        resultados = self.consultar_query(query, params)

        if resultados:
            for libro in resultados:
                print(f"ISBN: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Categoría: {libro[3]}")
        else:
            print("No se encontraron libros con los criterios especificados.")

    def listar_libros_prestados(self, id_usuario):
        """Mostrar una lista de todos los libros actualmente prestados a un usuario."""
        query = '''
        SELECT libros.isbn, libros.titulo, libros.autor, libros.categoria
        FROM libros
        JOIN libros_prestados ON libros.isbn = libros_prestados.isbn
        WHERE libros_prestados.id_usuario = ?
        '''
        resultados = self.consultar_query(query, (id_usuario,))
        
        if resultados:
            for libro in resultados:
                print(f"ISBN: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Categoría: {libro[3]}")
        else:
            print(f"El usuario con ID {id_usuario} no tiene libros prestados.")


def mostrar_menu():
    print("\nSistema de Gestión de Biblioteca Digital")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")

def main():
    biblioteca = Biblioteca()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-9): ")
        
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)
        
        elif opcion == '2':
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        
        elif opcion == '3':
            nombre = input("Ingrese el nombre del usuario: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.registrar_usuario(nombre, id_usuario)
        
        elif opcion == '4':
            id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)
        
        elif opcion == '5':
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.prestar_libro(isbn, id_usuario)
        
        elif opcion == '6':
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            id_usuario = input("Ingrese el ID del usuario: ")
            biblioteca.devolver_libro(isbn, id_usuario)
        
        elif opcion == '7':
            print("Opciones de búsqueda:")
            print("1. Por título")
            print("2. Por autor")
            print("3. Por categoría")
            opcion_busqueda = input("Seleccione una opción (1-3): ")
            
            if opcion_busqueda == '1':
                titulo = input("Ingrese el título del libro a buscar: ")
                biblioteca.buscar_libros(titulo=titulo)
            elif opcion_busqueda == '2':
                autor = input("Ingrese el autor del libro a buscar: ")
                biblioteca.buscar_libros(autor=autor)
            elif opcion_busqueda == '3':
                categoria = input("Ingrese la categoría del libro a buscar: ")
                biblioteca.buscar_libros(categoria=categoria)
            else:
                print("Opción no válida.")
        
        elif opcion == '8':
            id_usuario = input("Ingrese el ID del usuario para listar libros prestados: ")
            biblioteca.listar_libros_prestados(id_usuario)
        
        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 9.")

if __name__ == "__main__":
    main()
1