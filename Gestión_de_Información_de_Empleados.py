"""
Programa de Gestión de Información de Empleados

Este programa muestra información básica de un empleado, incluyendo nombre,
edad, salario y estado civil. Utiliza diferentes tipos de datos (string, integer,
float y boolean) para almacenar y mostrar la información.

"""


# Función para ingresar los datos del empleado
def ingresar_datos_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    salario = float(input("Ingrese el salario mensual del empleado: "))
    estado_civil = input("¿El empleado está casado? (s/n): ").lower()
    if estado_civil == "s":
        casado = True
    else:
        casado = False
    return nombre, edad, salario, casado


# Función para mostrar la información del empleado
def mostrar_informacion_empleado(nombre, edad, salario, casado):
    print("\nInformación del empleado:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad} años")
    print(f"Salario: ${salario}")
    if casado:
        print("Estado civil: Casado")
    else:
        print("Estado civil: Soltero")


# Función principal que ejecuta el programa
def main():
    # Solicitar al usuario que ingrese los datos del empleado
    nombre, edad, salario, casado = ingresar_datos_empleado()

    # Mostrar la información del empleado utilizando los datos ingresados
    mostrar_informacion_empleado(nombre, edad, salario, casado)


# Ejecutar la función principal si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()
