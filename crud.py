#Implementar Librerías básicas para la gestión del proyecto ABM -alta-baja-modificacion
#Librerias a usar:Django, PyMySQL, bcrypt(para encriptar contraseñas antes de mandarlas a la base de datos), Pytest, Pillow(para manejar imagenes), etc.
import pymysql

''' FUNCIONES GENERALES '''
# Funcion para obtener informacion de los disfraces
def obtener_disfraz(idDisfraz):
    # Consulta para obtener el disfraz
    query = 'SELECT * FROM stock WHERE idDisfraz = %s;'
    # Ejecutar la consulta y pasar los parámetros de manera segura
    cursor.execute(query, (idDisfraz,))
    # Obtener el resultado
    datos_disfraz = cursor.fetchone()  # Usar fetchone() para una sola fila
    # Verifico si se encontro el disfraz
    if datos_disfraz:
        print(f"Disfraz encontrado: {datos_disfraz}")
    else:
        print("No se encontró el disfraz con ese ID.")
    # Devuelvo los datos
    return datos_disfraz

# Funcion para pedir numeros enteros con manejo de errores
def pedir_entero(instrucciones):
    while True:
        try:
            numero = int(input(instrucciones))
            return numero
        except ValueError:
            print("Eso no es un valor válido. Por favor, intenta de nuevo.")

''' FUNCIONES ESPECIFICAS '''
# Función para que el cliente compre un disfraz
def comprar_disfraz():  
    while True:
        # Ingreso del ID del disfraz
        idDisfraz = pedir_entero('Ingrese el id del disfraz: ')
        # Obtengo los datos del disfraz
        datos_disfraz = obtener_disfraz(idDisfraz)
        cantidad,precioVenta = int(datos_disfraz[2]),datos_disfraz[3]
        
        # Verificamos el stock del disfraz
        if cantidad==0:
            print("No hay mas stock de ese disfraz")
            break
         
        # Precio a pagar
        print(f"El precio a pagar es {precioVenta}")    
        print("Venta realizada con exito!")
        
        # Modificamos la cantidad de disfraces
        try:
            query = "UPDATE stock SET cantidad = %s WHERE idDisfraz = %s;"
            # Ejecutar la consulta pasando los parámetros
            cursor.execute(query,(cantidad-1,idDisfraz))
            # Realizar commit para guardar los cambios en la base de datos
            connection.commit()
            print("Cantidad actualizada con éxito!")
        except:
            # ROLLBACK --> Vuelve atras y no efectua ningun cambio
            connection.rollback()
            print("No se pudo actualizar")
        finally:
            break
    
# Función para que el cliente alquile un disfraz
def alquilar_disfraz():
    while True:
        # Ingreso del ID del disfraz
        idDisfraz = pedir_entero('Ingrese el id del disfraz: ')
        # Obtengo los datos del disfraz
        datos_disfraz = obtener_disfraz(idDisfraz)
        cantidad,precio_alquilerXdia = int(datos_disfraz[2]),int(datos_disfraz[4])
        
        # Verificamos el stock del disfraz
        if cantidad==0:
            print("No hay mas stock de ese disfraz")
            break
        
        # Calculamos el precio del alquiler por la cantidad de dias
        dias = pedir_entero("Ingrese la cantidad de dias que quiere alquilar el disfraz: ")
        precio_alquiler_total = dias * precio_alquilerXdia
        print(f'El precio total a pagar es {precio_alquiler_total}')
        print("Alquiler realizado con exito!")
        
        # Modificamos la cantidad de disfraces
        try:
            query = "UPDATE stock SET cantidad = %s WHERE idDisfraz = %s;"
            # Ejecutar la consulta pasando los parámetros
            cursor.execute(query,(cantidad-1,idDisfraz))
            # Realizar commit para guardar los cambios en la base de datos
            connection.commit()
            print("Cantidad actualizada con éxito.")
        except:
            # ROLLBACK --> Vuelve atras y no efectua ningun cambio
            connection.rollback()
            print("No se pudo actualizar")
        finally:
            break

# Menú principal
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Comprar un disfraz")
        print("2. Alquilar un disfraz")
        print("3. Salir")
        
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
            print("Gracias por utilizar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    # Configuración de conexión a la base de datos
    connection = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="1234",database='disfraces')
    cursor = connection.cursor() 
    menu_principal()   
    # Cerrar la conexión
    connection.close()  

