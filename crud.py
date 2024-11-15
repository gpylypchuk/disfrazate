#Implementar Librerías básicas para la gestión del proyecto ABM -alta-baja-modificacion
#Librerias a usar:Django, PyMySQL, bcrypt(para encriptar contraseñas antes de mandarlas a la base de datos), Pytest, Pillow(para manejar imagenes), etc.
import pymysql

# Configuración de conexión a la base de datos
def conectar_bd():
    return pymysql.connect(host="127.0.0.1",port=3306,user="root",password="1234",database='disfraces')
    
# Actualización de stock y ganancias
def actualizar_stock_y_ganancias():
    # Aquí actualizarías el stock y ganancias en la base de datos
    pass

# Funciones específicas
def comprar_disfraz(): #Funcion para que el cliente compre un disfraz
    print("Función para comprar un disfraz.")
    # Conexión y lógica de compra
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            # Ejemplo de consulta: Actualizar stock y ganancias
            sql = "UPDATE disfraces SET stock = stock - 1 WHERE id = %s"
            cursor.execute(sql, (1,))  # Cambiar el ID por el seleccionado
            sql = "UPDATE ganancias SET total = total + %s WHERE id = 1"
            cursor.execute(sql, (100,))  # Cambiar 100 por el precio del disfraz
            conexion.commit()
    finally:
        conexion.close()

def alquilar_disfraz():
    print("Función para alquilar un disfraz.")
    # Conexión y lógica de alquiler
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            # Ejemplo de consulta: Actualizar disponibilidad y ganancias
            sql = "UPDATE disfraces SET disponible = 0 WHERE id = %s"
            cursor.execute(sql, (1,))  # Cambiar el ID por el seleccionado
            sql = "UPDATE ganancias SET total = total + %s WHERE id = 1"
            cursor.execute(sql, (50,))  # Cambiar 50 por el precio del alquiler
            conexion.commit()
    finally:
        conexion.close()

def devolver_disfraz():
    print("Función para devolver un disfraz.")
    # Conexión y lógica de devolución
    conexion = conectar_bd()
    try:
        with conexion.cursor() as cursor:
            # Ejemplo de consulta: Actualizar disponibilidad
            sql = "UPDATE disfraces SET disponible = 1 WHERE id = %s"
            cursor.execute(sql, (1,))  # Cambiar el ID por el seleccionado
            conexion.commit()
    finally:
        conexion.close()

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Comprar un disfraz")
        print("2. Alquilar un disfraz")
        print("3. Devolver un disfraz")
        print("4. Salir")
        
        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            comprar_disfraz()
        elif opcion == 2:
            alquilar_disfraz()
        elif opcion == 3:
            devolver_disfraz()
        elif opcion == 4:
            print("Gracias por utilizar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()