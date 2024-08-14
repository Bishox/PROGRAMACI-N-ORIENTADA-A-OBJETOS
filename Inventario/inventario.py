import sqlite3

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        # Conectar a la base de datos
        self.conn = sqlite3.connect('inventario.db')
        self.cursor = self.conn.cursor()

    def añadir_producto(self, producto):
        try:
            self.cursor.execute('''
                INSERT INTO productos (id, nombre, cantidad, precio)
                VALUES (?, ?, ?, ?)
            ''', (producto.id, producto.nombre, producto.cantidad, producto.precio))
            self.conn.commit()
            print(f"Producto añadido: {producto}")
        except sqlite3.IntegrityError:
            print(f"Error: Ya existe un producto con el ID {producto.id}.")

    def eliminar_producto(self, id):
        self.cursor.execute('DELETE FROM productos WHERE id = ?', (id,))
        if self.cursor.rowcount:
            self.conn.commit()
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"Error: No se encontró el producto con el ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        updates = []
        parameters = []
        
        if cantidad is not None:
            updates.append("cantidad = ?")
            parameters.append(cantidad)
        if precio is not None:
            updates.append("precio = ?")
            parameters.append(precio)
        
        if updates:
            sql = f'UPDATE productos SET {", ".join(updates)} WHERE id = ?'
            parameters.append(id)
            self.cursor.execute(sql, parameters)
            if self.cursor.rowcount:
                self.conn.commit()
                print(f"Producto actualizado: ID {id}")
            else:
                print(f"Error: No se encontró el producto con el ID {id}.")

    def buscar_producto_por_nombre(self, nombre):
        self.cursor.execute('SELECT * FROM productos WHERE nombre LIKE ?', ('%' + nombre + '%',))
        productos = self.cursor.fetchall()
        if productos:
            for prod in productos:
                print(f"ID: {prod[0]}, Nombre: {prod[1]}, Cantidad: {prod[2]}, Precio: {prod[3]}")
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        self.cursor.execute('SELECT * FROM productos')
        productos = self.cursor.fetchall()
        if productos:
            for prod in productos:
                print(f"ID: {prod[0]}, Nombre: {prod[1]}, Cantidad: {prod[2]}, Precio: {prod[3]}")
        else:
            print("No hay productos en el inventario.")

    def __del__(self):
        # Cerrar la conexión a la base de datos
        self.conn.close()

def imprimir_arte_ascii_inventario():
    arte_ascii = '''
     _________
     /         /|
    /_________/ |
   | _______  | |
   ||       || | |
   ||       || | |
   ||_______|| | |
   |_________|/  
   | INVENTARIO |
   |___________|               
    '''
    print(arte_ascii)

def obtener_numero_positivo(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor < 0:
                raise ValueError("El valor debe ser un número positivo.")
            return valor
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")

def obtener_numero_flotante(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

def menu():
    inventario = Inventario()
    
    while True:
        imprimir_arte_ascii_inventario()
        print("\nMenú de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            id = obtener_numero_positivo("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = obtener_numero_positivo("Ingrese cantidad del producto: ")
            precio = obtener_numero_flotante("Ingrese precio del producto: ")
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = obtener_numero_positivo("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = obtener_numero_positivo("Ingrese ID del producto a actualizar: ")
            cantidad_input = input("Ingrese nueva cantidad del producto (deje en blanco para no cambiar): ")
            precio_input = input("Ingrese nuevo precio del producto (deje en blanco para no cambiar): ")
            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 6.")

if __name__ == "__main__":
    menu()
