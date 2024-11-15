import pymysql

def open_connection():
    # abrir la conexion a la BD
    connection=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="1234",database='disfraces')
    # preparar el objeto cursor para posicionarse en alguna tabla
    cursor=connection.cursor()
    return cursor
