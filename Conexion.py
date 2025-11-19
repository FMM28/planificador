import os
import mariadb
from dotenv import load_dotenv

class MariaDB:
    def __init__(self, env_path=".env"):
        # Cargar archivo .env
        load_dotenv(env_path)

        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.db = os.getenv("DB_NAME", "")
        self.port = int(os.getenv("DB_PORT", "3306"))

        self.conn = None
        self.cursor = None

    def conectar(self):
        """Establece conexión con la base de datos."""
        try:
            self.conn = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            return True
        except mariadb.Error as e:
            print(f"Error de conexión a MariaDB: {e}")
            return False

    def cerrar(self):
        """Cierra cursor y conexión."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def ejecutar(self, query, params=None):
        """Ejecuta INSERT, UPDATE o DELETE."""
        try:
            self.cursor.execute(query, params or ())
            self.conn.commit()
            return self.cursor.rowcount
        except mariadb.Error as e:
            print(f"Error al ejecutar query: {e}")
            return None

    def consultar(self, query, params=None):
        """Ejecuta SELECT y devuelve los resultados."""
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except mariadb.Error as e:
            print(f"Error en la consulta: {e}")
            return None

    def __enter__(self):
        """Permite usar la clase con 'with'."""
        if not self.conectar():
            raise Exception("No se pudo conectar a la base de datos.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar()
