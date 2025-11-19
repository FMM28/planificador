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
df_salon_horario = df_salon_horario.sort_values(by=['peso','salon','hora'], ascending=[False,True,True]).reset_index(drop=True)
print(df_salon_horario)

#Calcular pesos de profesor-materia
## Parte de Angel 
# * primero consultar cuantas materias puede dar cada profesor: 
res = conn.consultar("""
SELECT p.id_prof, p.nombre, COUNT(pm.id_mat) AS total_materias
FROM profesor p
LEFT JOIN profesor_materia pm ON pm.id_prof = p.id_prof
GROUP BY p.id_prof, p.nombre
""")

df_prof_cant = pd.DataFrame(res, columns=['id_prof', 'nombre', 'total_materias'])
print(df_prof_cant)

# * Asignacion de pesos: 
df_prof_cant['peso'] = pd.cut(
    df_prof_cant['total_materias'],
    bins=[0, 1, 2, 3, 4, 100],  
    labels=[5,4,3,2,1]      
).astype(int)

df_prof = df_prof.merge(df_prof_cant[['id_prof', 'total_materias', 'peso']],
                        left_on='id_profesor', right_on='id_prof')

df_prof.drop(columns=['id_prof'], inplace=True)
df_prof.drop(columns=['id_profesor'], inplace=True)

print(df_prof)

conn.cerrar()

#----------- Asignacion de grupos ------------
print("Total de grupos por asignar:",sum(df_mat['grupos_mat'])+sum(df_mat['grupos_des']))

#Preparacion columnas soporte
df_prof['mat_asig'] = 0
df_salon_horario['grupo'] = None
df_salon_horario['materia'] = None
df_salon_horario['profesor'] = None

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

# Asignacion de profesores y salones

#Profesores
def obtener_profe_para_materia(materia, turno, priorizar_sin_carga=False):

    # 1. Obtener profesores que pueden dar esa materia
    posibles = df_prof_mat[df_prof_mat["materia"] == materia]["profesor"]

    # 2. Filtrar df_prof para esos profesores
    df = df_prof[df_prof["nombre"].isin(posibles)].copy()

    # 3. Filtrar por disponibilidad de turno
    if turno == "matutino":
        df = df[df["da_matutino"] == 1]
    elif turno == "vespertino":
        df = df[df["da_vespertino"] == 1]

    # 4. Filtrar profesores con carga disponible
    df = df[df["mat_asig"] < df["materias"]]

    if df.empty:
        return None

    # 5. Si se prioriza dar carga a profesores sin materias
    if priorizar_sin_carga:
        sin_carga = df[df["mat_asig"] == 0]
        if not sin_carga.empty:
            df = sin_carga

    # 6. Ordenar por mat_asig y por peso
    df = df.sort_values(by=['mat_asig', 'peso'], ascending=[True, False])

    # 7. Tomar el profesor con mayor prioridad
    return df.iloc[0]["nombre"]

def asignar_profesores():
    # Dos pasadas, la primera asegura que cada profesor tenga al menos una materia,
    # Segunda pasada reparte el resto de materias, y asigna grupos adicionales
    for idx, row in df_asig.iterrows():
        materia = row["materia"]
        turno = row["turno"]

        # Asignar priorizando profesores sin carga
        profesor = obtener_profe_para_materia(materia=materia, turno=turno, priorizar_sin_carga=True)

        if profesor is None:
            continue
        
        # Registrar el profesor en df_asig
        df_asig.loc[idx, "profesor"] = profesor
        
        # Actualizar mat_asig en df_prof
        df_prof.loc[df_prof["nombre"] == profesor, "mat_asig"] += 1
    
    # Completar asignaciones pendientes
    for idx, row in df_asig.iterrows():
        if pd.notna(row["profesor"]):
            continue
            
        materia = row["materia"]
        turno = row["turno"]

        # Intentar obtener profesor disponible
        profesor = obtener_profe_para_materia(materia=materia, turno=turno)

        # Si no hay profesor disponible con capacidad
        if profesor is None:
            # Buscar entre todos los que pueden dar la materia
            posibles = df_prof_mat[df_prof_mat["materia"] == materia]["profesor"]
            df_posibles = df_prof[df_prof["nombre"].isin(posibles)].copy()

            # Filtrar por turno
            if turno == "matutino":
                df_posibles = df_posibles[df_posibles["da_matutino"] == 1]
            elif turno == "vespertino":
                df_posibles = df_posibles[df_posibles["da_vespertino"] == 1]

            # Elegir al de mayor calificación pero menor carga
            df_posibles['carga'] = df_posibles['mat_asig'] / df_posibles['materias']
            df_posibles = df_posibles.sort_values(by=["carga", "calificacion"], ascending=[True, False])

            profesor = df_posibles.iloc[0]["nombre"]
            print(f"[EXTRA] {profesor} recibe una materia extra: {materia}")

        # Registrar el profesor en df_asig
        df_asig.loc[idx, "profesor"] = profesor
        
        # Actualizar mat_asig en df_prof
        df_prof.loc[df_prof["nombre"] == profesor, "mat_asig"] += 1

asignar_profesores()

#Salones y horarios
def asignar_horarios():
    for idx, row in df_asig.iterrows():
        materia = row['materia']
        profesor = row['profesor']
        grupo = row['grupo']
        turno_grupo = row['turno']

        # 1. Filtrar horarios disponibles por turno
        disponibles = df_salon_horario[(df_salon_horario['grupo'].isnull()) & (df_salon_horario['turno'] == turno_grupo)].copy()

        # 2. Evitar conflictos del profesor
        conflictos_prof = df_salon_horario[(df_salon_horario['profesor'] == profesor)][['hora','dias']]
        if not conflictos_prof.empty:
            disponibles = disponibles.merge(conflictos_prof,on=['hora','dias'],how='left',indicator=True)
            disponibles = disponibles[disponibles['_merge'] == 'left_only'].drop(columns=['_merge'])

        # 3. Evitar conflictos del mismo grupo
        conflictos_grupo = df_salon_horario[(df_salon_horario['grupo'] == grupo)][['hora','dias']]
        if not conflictos_grupo.empty:
            disponibles = disponibles.merge(conflictos_grupo,on=['hora','dias'],how='left',indicator=True)
            disponibles = disponibles[disponibles['_merge'] == 'left_only'].drop(columns=['_merge'])

        # 4. Si no hay disponibles, intentar intercambio de salon
        if disponibles.empty:
            # Buscar candidatos
            candidatos_intercambio = df_salon_horario[(df_salon_horario['grupo'].notnull()) & (df_salon_horario['turno'] == turno_grupo)].copy()
            
            # Filtrar para que el profesor no tenga conflicto
            if not conflictos_prof.empty:
                candidatos_intercambio = candidatos_intercambio.merge(conflictos_prof,on=['hora','dias'],how='left',indicator=True)
                candidatos_intercambio = candidatos_intercambio[candidatos_intercambio['_merge'] == 'left_only'].drop(columns=['_merge'])
            
            # Filtrar para que el grupo no tenga conflicto
            if not conflictos_grupo.empty:
                candidatos_intercambio = candidatos_intercambio.merge(conflictos_grupo,on=['hora','dias'],how='left',indicator=True)
                candidatos_intercambio = candidatos_intercambio[candidatos_intercambio['_merge'] == 'left_only'].drop(columns=['_merge'])
            
            intercambio_exitoso = False
            
            for _, candidato in candidatos_intercambio.iterrows():
                idx_candidato = candidato.name
                prof_candidato = candidato['profesor']
                grupo_candidato = candidato['grupo']
                materia_candidato = candidato['materia']
                
                disponibles_para_candidato = df_salon_horario[(df_salon_horario['grupo'].isnull()) & (df_salon_horario['turno'] == turno_grupo)].copy()
                conflictos_candidato = df_salon_horario[(df_salon_horario['profesor'] == prof_candidato)][['hora','dias']]
                if not conflictos_candidato.empty:
                    disponibles_para_candidato = disponibles_para_candidato.merge(conflictos_candidato,on=['hora','dias'],how='left',indicator=True)
                    disponibles_para_candidato = disponibles_para_candidato[disponibles_para_candidato['_merge'] == 'left_only'].drop(columns=['_merge'])
                conflictos_grupo_candidato = df_salon_horario[(df_salon_horario['grupo'] == grupo_candidato)][['hora','dias']]
                if not conflictos_grupo_candidato.empty:
                    disponibles_para_candidato = disponibles_para_candidato.merge(conflictos_grupo_candidato,on=['hora','dias'],how='left',indicator=True)
                    disponibles_para_candidato = disponibles_para_candidato[disponibles_para_candidato['_merge'] == 'left_only'].drop(columns=['_merge'])
                
                if not disponibles_para_candidato.empty:
                    nuevo_candidato = disponibles_para_candidato.iloc[0]
                    idx_nuevo = nuevo_candidato.name
                    salon_liberado = candidato['salon']
                    hora_liberada = candidato['hora']
                    dias_liberados = candidato['dias']
                    
                    df_salon_horario.at[idx_nuevo, 'grupo'] = grupo_candidato
                    df_salon_horario.at[idx_nuevo, 'materia'] = materia_candidato
                    df_salon_horario.at[idx_nuevo, 'profesor'] = prof_candidato
                    mask_asig = ((df_asig['profesor'] == prof_candidato) &(df_asig['grupo'] == grupo_candidato) &(df_asig['materia'] == materia_candidato))
                    df_asig.loc[mask_asig, 'salon'] = nuevo_candidato['salon']
                    df_asig.loc[mask_asig, 'hora'] = nuevo_candidato['hora']
                    df_asig.loc[mask_asig, 'dias'] = nuevo_candidato['dias']
                    
                    df_salon_horario.at[idx_candidato, 'grupo'] = grupo
                    df_salon_horario.at[idx_candidato, 'materia'] = materia
                    df_salon_horario.at[idx_candidato, 'profesor'] = profesor
                    df_asig.at[idx, 'salon'] = salon_liberado
                    df_asig.at[idx, 'hora'] = hora_liberada
                    df_asig.at[idx, 'dias'] = dias_liberados
                    
                    intercambio_exitoso = True
                    print(f"Se reasigno {prof_candidato}: {salon_liberado} {hora_liberada} {dias_liberados} a {nuevo_candidato['salon']} {nuevo_candidato['hora']} {nuevo_candidato['dias']}")
                    break
            
            if not intercambio_exitoso:
                print(f"No se pudo reasignar: {materia} - {profesor} - {grupo}")
            continue

        # 5. Seleccionar el horario con mayor peso
        disponibles = disponibles.sort_values(by=['peso', 'salon', 'hora'], ascending=[False, True, True])
        asignado = disponibles.iloc[0]

        # 6. Registrar en df_asig
        df_asig.at[idx, 'salon'] = asignado['salon']
        df_asig.at[idx, 'hora'] = asignado['hora']
        df_asig.at[idx, 'dias'] = asignado['dias']
        df_asig.at[idx, 'turno'] = asignado['turno']

        # 7. Marcar como ocupado en df_salon_horario
        mask = ((df_salon_horario['salon'] == asignado['salon']) & (df_salon_horario['hora'] == asignado['hora']) & (df_salon_horario['dias'] == asignado['dias']) & (df_salon_horario['turno'] == asignado['turno']))
        df_salon_horario.loc[mask, 'grupo'] = grupo
        df_salon_horario.loc[mask, 'materia'] = materia
        df_salon_horario.loc[mask, 'profesor'] = profesor

asignar_horarios()

# Exportación de datos
df_asig.to_csv('asignaciones.csv', index=False, encoding='utf-8')
df_salon_horario_export = df_salon_horario[['salon','hora','dias','turno','grupo','materia','profesor']].copy()
df_salon_horario_export['salon_sort'] = df_salon_horario_export['salon'].str.extract(r'[aA](\d+)')[0].astype(int)
df_salon_horario_export = df_salon_horario_export.sort_values(by=['salon_sort','salon','hora']).drop(columns=['salon_sort']).reset_index(drop=True)
df_salon_horario_export.to_csv('salones_horarios.csv', index=False, encoding='utf-8')
