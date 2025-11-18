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
df_prof['da_matutino'] = df_prof['da_matutino'].astype(bool)
df_prof['da_vespertino'] = df_prof['da_vespertino'].astype(bool)
df_prof.drop(columns=['id_profesor'], inplace=True)
print(df_prof)
print(df_prof.dtypes)

#Materias
columnas = ['semestre','nombre_materia']
res = conn.consultar(f"SELECT {','.join(columnas)} FROM materias")
df_mat = pd.DataFrame(res,columns=columnas)
df_mat['semestre'] = df_mat['semestre'].replace({'primero':1,'segundo':2,'tercero':3,'cuarto':4,'quinto':5,'sexto':6,'septimo':7,'octavo':8,'noveno':9})
df_mat['grupos_mat'] = df_mat['semestre'].apply(lambda x: 2 if x % 2 == 0 else 4)
df_mat['grupos_des'] = df_mat['semestre'].apply(lambda x: 2 if x % 2 == 0 else 4)
print(df_mat)
print(df_mat.dtypes)

#Materias por profesor
res = conn.consultar("SELECT m.nombre_materia AS materia, p.nombre AS profesor FROM profesor p JOIN profesor_materia pm ON pm.id_prof = p.id_prof JOIN materias m ON pm.id_mat = m.id;")
df_prof_mat = pd.DataFrame(res,columns=['materia','profesor'])
df_prof_mat = df_prof_mat.sort_values(by=['materia', 'profesor'])
df_prof_mat = df_prof_mat.reset_index(drop=True)
print(df_prof_mat)
print(df_prof_mat.dtypes)

#Salones y horarios
res = conn.consultar("SELECT salon FROM salones")
df_salones = pd.DataFrame(res,columns=['salon'])
res = conn.consultar("SELECT id_horario, hora, dias  FROM horarios")
df_horarios = pd.DataFrame(res,columns=['id_horario','hora','dias'])
df_horarios['turno'] = df_horarios['hora'].apply(lambda h: 'matutino' if int(h.split(':')[0]) < 14 else 'vespertino')
df_horarios.drop(columns=['id_horario'], inplace=True)
print(df_horarios)
df_salon_horario = df_salones.merge(df_horarios, how='cross')
print(df_salon_horario)
print(df_salon_horario.dtypes)

conn.cerrar()

#----------- Calculo de pesos ------------

def calcular_peso_salon(hora, turno, salon):
    # Extraer solo la hora
    hora_num = int(hora.split(':')[0])
    
    # Determinar el edificio del salon
    if salon.startswith('A2'):
        edificio = 'A2'
    elif salon.startswith('A5'):
        edificio = 'A5'
    elif salon.startswith('A8'):
        edificio = 'A8'
    elif salon.startswith('A11'):
        edificio = 'A11'
    
    # Peso base por horario
    peso_horario = 0
    if turno == 'matutino':
        if hora_num == 7:
            peso_horario = 100
        elif hora_num == 8:
            peso_horario = 90
        elif hora_num == 9:
            peso_horario = 80
        elif hora_num == 10:
            peso_horario = 70
        elif hora_num == 11:
            peso_horario = 60
        elif hora_num == 12:
            peso_horario = 50
        elif hora_num == 13:
            peso_horario = 40
        else:
            peso_horario = 30
    else: 
        if hora_num == 14:
            peso_horario = 100
        elif hora_num == 15:
            peso_horario = 90
        elif hora_num == 16:
            peso_horario = 80
        elif hora_num == 17:
            peso_horario = 70
        elif hora_num == 18:
            peso_horario = 60
        elif hora_num == 19:
            peso_horario = 50
        elif hora_num == 20:
            peso_horario = 40
        else:
            peso_horario = 30
    
    # Ajuste por edificio
    if edificio == 'A2':
        peso_horario += 20
    elif edificio == 'A5':
        peso_horario += 10
    elif edificio == 'A8':
        peso_horario += 0
    elif edificio == 'A11':
        peso_horario += -10
    
    return peso_horario

# Calcular pesos de salon-horario
df_salon_horario['peso'] = df_salon_horario.apply(lambda row: calcular_peso_salon(row['hora'], row['turno'], row['salon']), axis=1)
df_salon_horario = df_salon_horario.sort_values(['peso','salon','hora'], ascending=[False,True,True]).reset_index(drop=True)
print(df_salon_horario)

df_salon_horario.to_csv('salones_horarios.csv', index=False, encoding='utf-8')

#----------- Asignacion de grupos ------------
print("Total de grupos por asignar:",sum(df_mat['grupos_mat'])+sum(df_mat['grupos_des']))

#Preparacion columnas soporte
df_prof['mat_asig'] = 0

#DF de asignacion
grupos = []
for i in range(1,10):
    n = 2 if i % 2 == 0 else 4
    for j in range(1,n+1):
        grupo_id = f"1{i}0{j}"
        grupos.append((i,grupo_id,'matutino'))
        grupo_id = f"1{i}5{j}"
        grupos.append((i,grupo_id,'vespertino'))
grupos = pd.DataFrame(grupos,columns=['semestre','grupo','turno'])
grupos = grupos.sort_values(by=['semestre','turno']).reset_index(drop=True)     
print(grupos)

asignaciones = []
for idx, row in grupos.iterrows():
    semestre = row['semestre']
    grupo = row['grupo']
    turno = row['turno']
    
    materias_sem = df_mat[df_mat['semestre'] == semestre]['nombre_materia']
    
    for materia in materias_sem:
        asignaciones.append([grupo, materia, None, None, None, None, turno])
        
columnas_asig = ['grupo','materia','profesor','salon','hora','dias','turno']
df_asig = pd.DataFrame(asignaciones, columns=columnas_asig)
print(df_asig)
df_asig.to_csv('asignaciones.csv', index=False, encoding='utf-8')
