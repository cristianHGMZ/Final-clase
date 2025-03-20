import mysql.connector
from datetime import datetime

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",  # o "localhost"
            user="root",
            password="1234",
            database="eventos"
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)
        return None

def insertar_tipo_usuario(descripcion, estado):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO tipo_usuario (descripcion, estado) VALUES (%s, %s)", (descripcion, estado))
            conexion.commit()
            print("Tipo de usuario insertado correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar tipo de usuario:", error)
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()

def insertar_usuario(id_tipo_usuario, identificacion, nombre, correo, celular, estado):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO usuario (id_tipo_usuario, identificacion, nombre, correo, celular, estado) VALUES (%s, %s, %s, %s, %s, %s)",
                           (id_tipo_usuario, identificacion, nombre, correo, celular, estado))
            conexion.commit()
            print("Usuario insertado correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar usuario:", error)
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()

def insertar_evento(nombre, ciudad, fecha, aforo, ubicacion, valor_boleta):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO evento (nombre, ciudad, fecha, aforo, ubicacion, valor_boleta) VALUES (%s, %s, %s, %s, %s, %s)",
                           (nombre, ciudad, fecha, aforo, ubicacion, valor_boleta))
            conexion.commit()
            print("Evento insertado correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar evento:", error)
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()

def insertar_boleta(id_usuario, id_evento, estado, fecha_compra):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO boleta (id_usuario, id_evento, estado, fecha_compra) VALUES (%s, %s, %s, %s)",
                           (id_usuario, id_evento, estado, fecha_compra))
            conexion.commit()
            print("Boleta insertada correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar boleta:", error)
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()

# Ejemplo de uso:
insertar_tipo_usuario("Administrador", "A")
insertar_usuario(1, "123456789", "Juan Perez", "juan@example.com", "1234567890", "A")
fecha_evento = datetime(2023, 12, 31, 20, 0, 0)
insertar_evento("Concierto Año Nuevo", "Bogotá", fecha_evento, 500, "Estadio", 100.00)
fecha_compra = datetime.now()
insertar_boleta("123456789", 1, "V", fecha_compra)
        