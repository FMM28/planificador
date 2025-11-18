SET NAMES 'UTF8MB4';
DROP DATABASE IF EXISTS horarios;
CREATE DATABASE IF NOT EXISTS horarios DEFAULT CHARACTER SET UTF8MB4;
USE horarios;

CREATE TABLE profesor(
	id_prof INT PRIMARY KEY NOT NULL auto_increment,
	nombre VARCHAR(50) NOT NULL,
	da_matutino BOOLEAN NOT NULL,
	da_vespertino BOOLEAN NOT NULL,
	calificacion FLOAT NOT NULL
);

INSERT INTO profesor(nombre, da_matutino, da_vespertino, calificacion) VALUES
("ABURTO CAMACHO BLANCA PAMELA", 0, 1, 10),
("AGUILAR HERNANDEZ JOSE FRANCISCO", 0, 1, 1),
("ALBA VILLA BELEN ANAID", 0, 1, 4.7),
("ALMANZAR VAZQUEZ MARIA GUADALUPE", 0, 1, 7.8),
("ALVAREZ SORIANO MANUEL ALEJANDRO", 0, 1, 10),
("ANAYA MANILA DZOARA IVETTE", 0, 1, 7),
("ARELLANO OROZCO JUAN MANUEL", 1, 0, 5),
("ARELLANO RIVERA ESTEBAN", 0, 1, 8.2),
("AYALA PEÑA ESTEBAN", 0, 1, 4.5),
("BERNAL DIAZ ARCELIA ", 1, 0, 6.3),
("BLANCO BAUTISTA ROBERTO", 1, 0, 4.1),
("CAMACHO ALVAREZ JUAN CARLOS", 1, 1, 4.9),
("CAMPOS BRAVO JORGE IVAN", 0, 1, 5.5),
("CANDELARIO ALAVEZ JORGE LUIS", 1, 1, 9.2),
("CANTO GALLO RAFAEL", 1, 1, 6.4),
("CERVANTES PATIÑO MOISES", 0, 1, 4.5),
("CHIAPA MONROY CUAUHTEMOC", 0, 1, 3.6),
("COLUNGA VAZQUEZ MATILDE", 0, 1, 8.4),
("CRUZ LUEVANO BLANCA ESTELA", 0, 1, 6.3),
("FALCON ARELLANO BERENICE ITZEL", 0, 1, 9),
("FERIA VICTORIA MARIA ANGELICA", 1, 0, 6.6),
("GALICIA RANGEL GILDA", 1, 0, 3.2),
("GARCIA GUZMAN ENRIQUE", 1, 1, 3.5),
("GARCIA MONROY JOSE ANTONIO", 1, 0, 8.2),
("GARCIA VILLANUEVA MA. DEL PILAR", 1, 0, 7.2),
("GARIBAY PEDRAZA ALMA LILIA", 0, 1, 9.5),
("GASTALDI PEREZ JUAN", 1, 0, 8),
("GERMAN ROSAS CESAR FRANCISCO", 1, 0, 7.1),
("GONZALEZ AYALA LUIS ENRIQUE", 1,0,5.2),
("GONZALEZ BETANCOURT RAFAEL", 0, 1, 8.4),
("GONZALEZ HERNANDEZ GERARDO", 1, 0, 8.2),
("GONZALEZ HERNANDEZ MARIA GABRIELA", 1, 1, 6.1),
("GONZALEZ MAXINEZ DAVID JAIME", 1, 1, 5.8),
("GOYTIA HERRERA MARCO INTI", 0, 1, 9),
("GRADA HUERTA IVAN", 0, 1, 7.4),
("GUERRERO SANTAMARIA EFREN", 0, 1, 10),
("GUTIERREZ CASTILLO ALMA ROSA", 1, 1, 7.8),
("GUTIERREZ LOPEZ FELIPE DE JESUS", 0, 1, 10),
("GUTIERREZ OROZCO RICARDO ARTURO", 1, 1, 6),
("HERNANDEZ AUDELO LEOBARDO", 1, 0, 5.6),
("HERNANDEZ CABRERA JESUS", 1, 1, 9.3),
("HERNANDEZ CONTRERAS JUAN MANUEL", 0, 1, 8.5),
("HERNANDEZ GALICIA SALOMON", 0, 1, 8.7),
("HERNANDEZ HERNANDEZ MARTIN", 1, 0, 5.3),
("HERNANDEZ LOPEZ SERGIO", 1, 0, 7),
("ISLAS HERNANDEZ CLARA YAHAIRA", 0, 1, 4),
("JUAREZ PALMA JOSE GIL", 0, 1, 5.6),
("JUAREZ ROBLES ELIZABETH", 1, 1, 7.2),
("LOPEZ CARRETO JUAN MANUEL", 0, 1, 9.1),
("LOZANO MENDEZ EFREN", 0, 1, 5.4),
("MARTINEZ ROMERO JONATHAN", 1, 1, 9.4),
("MENDOZA GONZALEZ OMAR", 1, 1, 6.9),
("MONDRAGON ESCOBAR ALFREDO", 1, 1, 6),
("MONTERROSA ESCOBAR AMILCAR AMADO", 0, 1, 6),
("MORALES GONZALEZ JORGE CARLOS", 0, 1, 8.5),
("MORALES PALAFOX EDGAR", 0, 1, 4.9),
("NAVARRO DIAZ RAMON", 1, 0, 3.4),
("NERIA OROZCO ERIK DE JESUS", 1, 0, 7),
("OCAMPO ALVAREZ ARTURO", 0, 1, 3.5),
("OLIVER MORALES CARLOS", 1, 0, 5.7),
("ORDOÑEZ ROSALES MARTIN", 1, 0, 4.8),
("ORTEGA NAVA CARLOS FERNANDO", 1, 0, 5.9),
("ORTIZ CORDERO GABRIEL", 1, 1, 5.3),
("ORTIZ JIMENEZ MARIA ELENA", 1, 0, 4.4),
("PALMA LOPEZ DANIEL FERNANDO", 1, 0, 9),
("PARRALES CASTAÑEDA CARLOS ALBERTO", 0, 1, 5.2),
("PATIÑO RODRIGUEZ RAMON", 1, 1, 5.5),
("PELCASTRE RAMIREZ GLORIA SAMANTHA", 0, 1, 2),
("PEÑALOZA ROMERO ERNESTO", 1, 0, 8.8),
("PEREZ GUZMAN ALEJANDRO", 1, 1, 9.1),
("PEREZ MEDEL MARCELO", 0, 1, 10),
("PEREZ MUÑOZ ANTONIO GERARDO", 1, 0, 8),
("PEREZ PAZ EDUARDO", 0, 1, 1),
("PEREZ VALDES JOEL ALFREDO", 1, 0, 4.5),
("PICCINELLI BOCCHI GABRIELLA", 0, 1, 7.9),
("QUINTERO CERVANTES JOSE MANUEL", 1, 0, 6.1),
("QUIROZ ALMARAZ SERGIO", 0, 1, 7.3),
("RAMIREZ CRUZ JOSE LUIS", 1, 0, 7.4),
("RAMIREZ LAZOS ESTEBAN", 0, 1, 9.5),
("RAMOS MARQUEZ JUAN CARLOS", 0, 1, 9.5),
("REYES CRUZ ANA CLAUDIA", 1, 0, 10),
("REYES TECONTERO NORMA", 0, 1, 7.4),
("RODRIGUEZ GARCIA ARTURO", 0, 1, 9.2),
("ROMERO ANDALON JESUS ANGEL", 1, 1, 6.8),
("ROMERO UGALDE MARTIN MANUEL", 1, 1, 4.9),
("SANCHEZ HERNANDEZ MIGUEL ANGEL", 1, 1, 7.5),
("SANCHEZ MORALES VICTOR MANUEL", 1, 1, 5),
("SEGURA RAUDA MINERVA", 0, 1, 6.2),
("SOBERANES JAIME ROBERTO MISAEL", 0, 1, 7.2),
("SOLIS ALCANTAR EVERARDO", 0, 1, 5.9),
("SUAREZ HERRERA ALEJANDRO", 1, 1, 8.3),
("TORRES RODRIGUEZ GERARDO", 0, 1, 6.6),
("TORRES TORRES FAUSTO", 0, 1, 6.5),
("UGALDE LOPEZ JUDITH", 0, 1, 10),
("VAZQUEZ MORALES RODOLFO", 1, 0, 6.9),
("VELASCO AGUSTIN AARON", 1, 1, 8.9),
("VERDE CRUZ ABEL", 1, 1, 7),
("VERDUZCO RODRIGUEZ MARIANA", 1, 0, 8.8),
("VIDAL CASTRO RICARDO ADOLFO", 1, 0, 7.5),
("VIEYRA REBOYO LUIS ARMANDO", 1, 0, 6.2);

-- Ernesto
CREATE TABLE materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    semestre ENUM(
        'primero', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto', 'septimo', 'octavo', 'noveno') NOT NULL,
    creditos INT NOT NULL,
    nombre_materia VARCHAR(150) NOT NULL,
    clave_materia VARCHAR(50) NOT NULL UNIQUE
);
-- INSERT DE DATOS 
-- PRIMER
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('primero', 9, 'GEOMETRIA ANALITICA', '1108'),
('primero', 9, 'CALCULO DIFERENCIAL E INTEGRAL', '1109'),
('primero', 9, 'ALGEBRA', '1110'),
('primero', 9, 'COMPUTADORAS Y PROGRAMACION', '1111'),
('primero', 6, 'INTRODUCCION A LA INGENIERIA EN COMPUTACION', '1112');

-- SEGUNDO
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('segundo', 9, 'ALGEBRA LINEAL', '0062'),
('segundo', 9, 'CALCULO VECTORIAL', '0063'),
('segundo', 8, 'PROGRAMACION ORIENTADA A OBJETOS', '1203'),
('segundo', 8, 'COMUNICACION', '1209'),
('segundo', 8, 'EMPRENDIMIENTO 1', '1210'),
('segundo', 3, 'TALLER DE CREATIVIDAD E INNOVACION', '1211');

-- TERCER
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('tercero', 11, 'ELECTRICIDAD Y MAGNETISMO (L)', '0071'),
('tercero', 8, 'ESTRUCTURA DE DATOS', '0190'),
('tercero', 9, 'METODOS NUMERICOS', '0480'),
('tercero', 9, 'ECUACIONES DIFERENCIALES', '1303'),
('tercero', 8, 'EMPRENDIMIENTO 2', '1311');

-- CUARTO
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('cuarto', 9, 'PROBABILIDAD Y ESTADISTICA', '0712'),
('cuarto', 8, 'BASES DE DATOS 1', '1417'),
('cuarto', 8, 'EMPRENDIMIENTO 3', '1418'),
('cuarto', 9, 'MATEMATICAS DISCRETAS', '1419'),
('cuarto', 10, 'DISPOSITIVOS ELECTRONICOS (L)', '1522');

-- QUINTO
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('quinto', 8, 'LENGUAJES FORMALES Y AUTOMATAS', '0442'),
('quinto', 9, 'DISEÑO Y ANALISIS DE ALGORITMOS', '1500'),
('quinto', 8, 'ADMINISTRACION DE PROYECTOS', '1503'),
('quinto', 9, 'PROGRAMACION WEB 1', '1504'),
('quinto', 10, 'DISEÑO LOGICO (L)', '1521');

-- SEXTO
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('sexto', 8, 'COMPILADORES', '0434'),
('sexto', 8, 'SISTEMAS OPERATIVOS', '0840'),
('sexto', 10, 'DISEÑO DE SISTEMAS DIGITALES (L)', '1604'),
('sexto', 8, 'INGENIERIA DE SOFTWARE', '1605');

-- SEPTIMO
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('septimo', 8, 'SISTEMAS DE INFORMACION', '0789'),
('septimo', 9, 'PROGRAMACION WEB 2', '1718'),
('septimo', 10, 'REDES DE COMPUTADORAS 1 (L)', '1719'),
('septimo', 10, 'MICROPROCESADORES Y MICROCONTROLADORES (L)', '1800');

-- OCTAVO
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('octavo', 8, 'BASES DE DATOS 2', '1810'),
('octavo', 9, 'PROGRAMACION MOVIL 1', '1812'),
('octavo', 8, 'REDES DE COMPUTADORAS 2', '1813'),
('octavo', 8, 'HABILIDADES DIRECTIVAS', '1917');

-- NOVENO
INSERT INTO materias (semestre, creditos, nombre_materia, clave_materia) VALUES
('noveno', 8, 'INTELIGENCIA ARTIFICIAL', '0406'),
('noveno', 8, 'SEGURIDAD INFORMATICA', '1705'),
('noveno', 8, 'MINERIA DE DATOS', '1908');

-- Horario de materias 
CREATE TABLE horarios (
    id_horario INT PRIMARY KEY AUTO_INCREMENT,
    hora VARCHAR(15) NOT NULL,
    dias VARCHAR(3) NOT NULL
);
-- INSERT DE DATOS 

INSERT INTO horarios (hora, dias) VALUES
('07:00-8:20', 'LMV'),
('08:40-10:00', 'LMV'),
('10:00-11:20', 'LMV'),
('11:40-13:00', 'LMV'),
('13:00-14:20', 'LMV'),
('14:40-16:00', 'LMV'),
('16:00-17:20', 'LMV'),
('17:40-19:00', 'LMV'),
('19:00-21:20', 'LMV'),

('07:00-9:00', 'MJ'),
('09:00-11:00', 'MJ'),
('11:00-13:00', 'MJ'),
('13:00-15:00', 'MJ'),
('15:00-17:00', 'MJ'),
('17:00-19:00', 'MJ'),
('19:00-21:00', 'MJ');

CREATE TABLE profesor_materia(
    id_prma INT PRIMARY KEY NOT NULL auto_increment,
    id_prof INT NOT NULL,
    id_mat INT NOT NULL,
    FOREIGN KEY (id_prof) REFERENCES profesor(id_prof),
    FOREIGN KEY (id_mat) REFERENCES materias(id)
);

INSERT INTO profesor_materia(id_prof,id_mat) VALUES
(1,11),
(2,40),
(3,24),
(4,9),
(5,12),
(6,33),
(7,5),
(8,26),
(9,28),
(10,26),
(10,34),
(11,13),
(11,14),
(11,15),
(12,23),
(12,25),
(12,36),
(13,22),
(14,4),
(14,5),
(14,8),
(14,25),
(14,31),
(14,34),
(15,41),
(16,19),
(17,11),
(18,10),
(18,16),
(19,8),
(19,13),
(19,30),
(19,31),
(20,6),
(21,10),
(21,38),
(22,33),
(23,33),
(23,37),
(24,33),
(24,37),
(25,16),
(25,19),
(26,38),
(27,4),
(28,35),
(29,24),
(30,1),
(30,14),
(30,15),
(31,2),
(31,7),
(31,15),
(32,28),
(32,30),
(33,26),
(33,29),
(33,34),
(34,41),
(35,5),
(36,24),
(36,38),
(37,16),
(37,19),
(38,36),
(39,27),
(39,31),
(40,40),
(41,4),
(41,13),
(41,23),
(41,32),
(42,34),
(43,2),
(44,29),
(45,3),
(45,12),
(45,17),
(46,9),
(47,15),
(48,22),
(48,39),
(48,41),
(49,21),
(49,26),
(50,26),
(50,29),
(50,34),
(51,1),
(51,14),
(51,15),
(51,34),
(52,31),
(52,35),
(52,41),
(53,9),
(53,16),
(53,24),
(54,39),
(55,14),
(56,39),
(57,40),
(58,40),
(59,34),
(60,22),
(60,23),
(60,39),
(61,18),
(61,27),
(62,21),
(63,3),
(63,20),
(63,22),
(64,25),
(65,40),
(66,5),
(67,1),
(67,26),
(68,2),
(68,17),
(69,4),
(69,13),
(70,6),
(70,12),
(70,14),
(71,23),
(72,33),
(73,25),
(74,11),
(75,12),
(76,33),
(77,23),
(77,37),
(78,26),
(79,2),
(79,3),
(79,14),
(80,4),
(80,32),
(81,24),
(82,16),
(82,38),
(83,1),
(83,2),
(83,15),
(83,20),
(84,10),
(84,24),
(85,39),
(86,13),
(86,23),
(86,32),
(86,41),
(87,4),
(87,7),
(87,13),
(87,22),
(87,23),
(87,32),
(88,12),
(89,18),
(89,35),
(89,40),
(90,1),
(90,6),
(91,12),
(92,33),
(92,37),
(93,17),
(94,38),
(95,28),
(95,40),
(96,5),
(96,25),
(96,31),
(96,32),
(97,2),
(97,12),
(97,15),
(98,31),
(98,32),
(98,40),
(99,24),
(100,1),
(100,3),
(100,14);

CREATE TABLE salones (
    id_salon VARCHAR(10) NOT NULL,
    horario VARCHAR(50) NULL,
    PRIMARY KEY (id_salon)
);

INSERT INTO salones (id_salon, horario) VALUES ('A203', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A204', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A205', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A211', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A212', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A213', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A214', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A215', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A221', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A222', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A223', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A224', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A225', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A504', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A505', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A506', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A507', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A508', NULL);

INSERT INTO salones (id_salon, horario) VALUES ('A811', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A812', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A813', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A814', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A815', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A816', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A817', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A818', NULL);
INSERT INTO salones (id_salon, horario) VALUES ('A819', NULL);