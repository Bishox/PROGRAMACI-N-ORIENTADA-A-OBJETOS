import sqlite3

def inicializar_db():
    # Conectar a la base de datos (se crea si no existe)
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    # Crear la tabla 'productos' si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == "__main__":
    inicializar_db()
