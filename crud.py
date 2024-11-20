#Implementar Librerías básicas para la gestión del proyecto ABM -alta-baja-modificacion
#Librerias a usar:Django, PyMySQL, bcrypt(para encriptar contraseñas antes de mandarlas a la base de datos), Pytest, Pillow(para manejar imagenes), etc.
import pymysql
import re 

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

# Funcion para solicitar el dni
def solicitar_dni():
    while True:
        # Solicitar el DNI
        dni = input("Introduce tu DNI (solo números, 8 caracteres): ")
        
        # Validar que el DNI tenga exactamente 8 dígitos y que solo contenga números
        if len(dni) == 8 and dni.isdigit():
            return dni  # Si el DNI es válido, lo devolvemos y salimos
        else:
            print("DNI no válido. Asegúrate de que tenga exactamente 8 dígitos y contenga solo números.")

# Funcion para solicitar el email
def solicitar_email():
    while True:
        # Solicitar el email
        email = input("Introduce tu email: ")
        
        # Validar el formato del email usando expresión regular
        patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(patron_email, email):
            return email  # Si el email es válido, lo devolvemos y salimos
        else:
            print("Email no válido. Asegúrate de que tenga un formato correcto (ejemplo@dominio.com).")

# Funcion para solicitar el telefono
def solicitar_telefono():
    while True:
        telefono = input("Ingrese su número de teléfono (solo dígitos, 10 caracteres): ")
        
        # Validar que el teléfono contenga solo dígitos y tenga 10 caracteres
        if re.match(r'^\d{10}$', telefono):
            return telefono
        else:
            print("Número de teléfono inválido. Asegúrese de ingresar 10 dígitos.")

# Funcion para solicitar la contraseña
def solicitar_contraseña():
    while True:    
        # Solicitar la contraseña
        password = input("Introduce tu contraseña (mínimo 8 caracteres, con letras y números): ")
        
        # Validar que la contraseña tenga al menos 8 caracteres, incluyendo letras y números
        if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
            return password  # Si la contraseña es válida, la devolvemos y salimos
        else:
            print("Contraseña no válida. Asegúrate de que tenga al menos 8 caracteres y contenga tanto letras como números.")

# Funcion para obtener los datos del usuario
def obtener_usuario(mail):
    # Consulta para obtener el usuario
    query = 'SELECT * FROM clientes WHERE mail = %s;'
    # Ejecutar la consulta y pasar los parámetros de manera segura
    cursor.execute(query, (mail))
    # Obtener el resultado
    datos_disfraz = cursor.fetchone()  # Usar fetchone() para una sola fila
    # Verifico si se encontro el disfraz
    if datos_disfraz:
        print(f"Disfraz encontrado: {datos_disfraz}")
    else:
        print("No se encontró el disfraz con ese ID.")
    # Devuelvo los datos
    return datos_disfraz

''' FUNCIONES ESPECIFICAS '''
'''USUARIO'''
# Funcion para dar de alta un nuevo usuario
def nuevo_usuario():
    # Solicitamos y validamos los datos del usuario
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    dni = solicitar_dni()
    email = solicitar_email()
    telefono = solicitar_telefono()
    password = solicitar_contraseña()
    
    # GUARDAMOS LOS DATOS EN LA BD
    try:
        # Consulta SQL con parámetros para evitar inyección SQL
        query = """
            INSERT INTO Usuarios (dni, name, apellidos, email, telefono, contrasena) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Ejecutar la consulta con los valores correspondientes
        cursor.execute(query, (dni, nombre, apellido, email, telefono, password))
        connection.commit()
    except Exception as e:
        # Si ocurre un error, se hace rollback
        connection.rollback()
        print(f"Error al insertar los datos: {e}")

# Funcion para dar de baja un usuario
def eliminar_usuario():
    try:
        # Solicitamos el DNI del usuario
        dni = solicitar_dni()
        # Definimos la consulta SQL para eliminar al usuario
        query = "DELETE FROM clientes WHERE dni = %s"
        # Ejecutamos la consulta con el DNI proporcionado
        cursor.execute(query, (dni,))
        # Confirmamos los cambios en la base de datos
        connection.commit()
        print(f'Usuario con DNI {dni} eliminado correctamente.')
    except Exception as e:
        # Si ocurre un error, hacemos rollback y mostramos el error
        connection.rollback()
        print(f'Error al eliminar el usuario: {e}')

# Funcion para iniciar sesion
def iniciar_sesion():
    email = solicitar_email()
    password = solicitar_contraseña()
    datos_usuario = obtener_usuario(email)
    print('Los datos del usuario son: ',datos_usuario)

'''DISFRACES'''
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

''' MENU PRINCIPAL COMPRA Y USUARIO'''
def menu_principal_usuario():
    while True:
        print("\n--- Menú Principal Usuario ---")
        print("1. Crear nueva cuenta / Registrarme")
        print("2. Iniciar Sesion")
        print("3. Eliminar Cuenta")
        print("4. Salir")
        
        try:
            opcion = int(input("Elija una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            nuevo_usuario()
        elif opcion == 2:
            iniciar_sesion()
        elif opcion == 3:
            eliminar_usuario()
        elif opcion == 4:
            print("Gracias por utilizar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_principal_compra():
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
    menu_principal_usuario()
    menu_principal_compra()   
    # Cerrar la conexión
    connection.close()  