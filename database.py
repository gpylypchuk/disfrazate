import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",         # Cambia por tu configuración
            user="tu_usuario",
            password="tu_contraseña",
            database="TiendaDisfraces"
        )
        return connection
    except Error as e:
        print("Error al conectarse a la base de datos:", e)
        return None
