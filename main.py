from Conexion import MariaDB
import pandas as pd

#----------- Conexion a la BD ------------
conn = MariaDB()
conn.conectar()

#----------- Preparacion de los datos ------------

#Profesores
res = conn.consultar("SELECT * FROM profesor")
df_prof = pd.DataFrame(res,columns=['id_profesor','nombre','da_matutino','da_vespertino','calificacion'])
df_prof['materias'] = pd.cut(df_prof['calificacion'], bins=[0,2,4,6,8,10], labels=[1,2,3,4,5])
df_prof['materias'] = df_prof['materias'].astype(int)
df_prof.drop(columns=['id_profesor'], inplace=True)
print(df_prof)

#Materias
columnas = ['semestre','nombre_materia']
res = conn.consultar(f"SELECT {','.join(columnas)} FROM materias")
df_mat = pd.DataFrame(res,columns=columnas)
df_mat['semestre'] = df_mat['semestre'].replace({'primero':1,'segundo':2,'tercero':3,'cuarto':4,'quinto':5,'sexto':6,'septimo':7,'octavo':8,'noveno':9})
df_mat['grupos_mat'] = df_mat['semestre'].apply(lambda x: 2 if x % 2 == 0 else 4)
df_mat['grupos_des'] = df_mat['semestre'].apply(lambda x: 2 if x % 2 == 0 else 4)
print(df_mat)

conn.cerrar()

