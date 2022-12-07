CREATE TYPE tipo_usuario AS ENUM ('administrador', 'asistente', 'cliente');
CREATE TYPE status AS ENUM ('activo', 'inactivo');

CREATE TABLE usuarios (
	id serial PRIMARY KEY,
	nombre varchar(150) NOT NULL,
	email varchar(100) NOT NULL,
	clave varchar(100) NOT NULL,
	estado status NOT NULL,
	rol tipo_usuario NOT NULL
);


CREATE TABLE productos (
	id serial PRIMARY KEY,
	nombre varchar(100) NOT NULL,
	precio integer NOT NULL,
	direccion_proveedor varchar(100),
	url_origen varchar(300) NOT NULL,
	url_imagen varchar(300) NOT NULL
);

CREATE TABLE noticias (
	id serial PRIMARY KEY,
	titulo varchar(100) NOT NULL,
	descripcion varchar NOT NULL,
	url_multimedia varchar(300),
	estado status NOT NULL
);

INSERT INTO usuarios (nombre, email, clave, estado, rol)
VALUES ('El Admin', 'admin@mail.com', '123', 'activo', 'administrador');

