DROP DATABASE IF EXISTS twitter;
CREATE DATABASE twitter;
USE twitter;

DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario(
id INT auto_increment PRIMARY KEY,
nombre varchar(10) NOT NULL UNIQUE,
clave varchar(10) NOT NULL);

/*Me equivoque en la longitud de estos dos campos, por eso los cambio*/
ALTER TABLE usuario MODIFY nombre varchar(20);
ALTER TABLE usuario MODIFY clave varchar(20);

DROP TABLE IF EXISTS publicaciones;
CREATE TABLE publicaciones(
idUsuario INT,
FOREIGN KEY(idUsuario) REFERENCES usuario(id),
id INT auto_increment PRIMARY KEY,
publicacion varchar(280),
fecha DATETIME);

DROP PROCEDURE IF EXISTS verificarUsuario;
DELIMITER &&
CREATE PROCEDURE verificarUsuario(in nUsuario varchar(10))
BEGIN
	SELECT nombre FROM usuario WHERE nombre = nUsuario;
END &&

DROP PROCEDURE IF EXISTS verificarUsuarioYClave;
DELIMITER &&
CREATE PROCEDURE verificarUsuarioYClave(in nUsuario varchar(10), in pass varchar(10))
BEGIN
	SELECT nombre,clave FROM usuario WHERE nombre = nUsuario AND clave = pass;
END &&

DROP PROCEDURE IF EXISTS registrarUsuario;
DELIMITER &&
CREATE PROCEDURE registrarUsuario(in nUsuario varchar(10), in pass varchar(10))
BEGIN
	INSERT INTO usuario(nombre,clave) VALUES(nUsuario,pass);
END &&


DROP PROCEDURE IF EXISTS escribirPost;
DELIMITER &&
CREATE PROCEDURE escribirPost(in id int, in post varchar(180))
BEGIN
	INSERT INTO publicaciones(idUsuario, publicacion, fecha)
    VALUES(id,post,now());
END &&

DROP PROCEDURE IF EXISTS buscarUsuario;
DELIMITER &&
CREATE PROCEDURE buscarUsuario(in nombreUsuario varchar(20))
BEGIN
	SELECT nombre, publicacion, fecha FROM vistaPublicacion
    WHERE nombre LIKE CONCAT('%',nombreUsuario,'%');
END &&

DROP VIEW IF EXISTS vistaPublicacion;
CREATE VIEW vistaPublicacion
AS
select p.id, u.nombre, p.publicacion, p.fecha
FROM publicaciones as p
inner join usuario as u
on u.id = p.idUsuario;


