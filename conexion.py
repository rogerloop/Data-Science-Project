# Creación de un pool de connexión

# import para variables de entorno seguras y protegidas
from dotenv import load_dotenv
import os

from mysql.connector import pooling     # importamos el objeto pooling para usar posteriormente
from mysql.connector import Error      # importamos el objeto Error para procesar errores de conexion

load_dotenv()  # Carga las variables de entorno del archivo .env

class Conexion:
    DATABASE = os.getenv('DB_NAME')
    USERNAME = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = int(os.getenv('DB_PORT'))
    HOST = os.getenv('DB_HOST')
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrió un error al obtener el pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

# prueba funcionamiento app

if __name__ == '__main__':
    #creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')