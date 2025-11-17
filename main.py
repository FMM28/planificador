from Conexion import MariaDB

conn = MariaDB()
conn.conectar()
res = conn.consultar("SELECT * FROM profesor")
print(res)
conn.cerrar()