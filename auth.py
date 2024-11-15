import bcrypt
from database import get_connection

# Registrar un usuario
def registrar_usuario(nombre_usuario, nombre, apellido, correo, contraseña):
    # Hashear la contraseña
    contraseña_hash = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
    
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO Usuarios (nombre_usuario, nombre, apellido, correo, contraseña_hash)
                VALUES (%s, %s, %s)
            """, (nombre_usuario, nombre, apellido, correo, contraseña_hash.decode('utf-8')))
            connection.commit()
            return {"mensaje": "Usuario registrado exitosamente."}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()

# Iniciar sesión
def iniciar_sesion(nombre_usuario, contraseña):
    connection = get_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            # Buscar al usuario por nombre
            cursor.execute("""
                SELECT * FROM Usuarios WHERE nombre_usuario = %s
            """, (nombre_usuario,))
            usuario = cursor.fetchone()
            
            if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario['contraseña_hash'].encode('utf-8')):
                return {"mensaje": "Inicio de sesión exitoso.", "usuario": usuario['nombre_usuario']}
            else:
                return {"error": "Credenciales incorrectas."}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()
