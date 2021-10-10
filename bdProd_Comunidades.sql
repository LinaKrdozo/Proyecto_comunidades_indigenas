CREATE DATABASE Prod_comunidades;
CREATE SCHEMA datos_prod_comunidades;

CREATE TABLE Comunidades(
	id_comunidades serial PRIMARY KEY,
	nombre varchar(50)NOT NULL,
	region varchar(50)NOT NULL
);


CREATE TABLE Tipo_Producto(
	id_Tipo_Producto serial PRIMARY KEY,
	nombre_Tipo_Producto varchar(50)NOT NULL
);

CREATE TABLE Productos(
	id_productos serial PRIMARY KEY,
	tipo_producto_fk int NOT NULL,
	nombreProductos varchar(50)NOT NULL,
	caracteristicas varchar(50)NOT NULL,
	cantidad int NOT NULL,
	FOREIGN KEY(tipo_producto_fk) REFERENCES Tipo_Producto(id_Tipo_Producto)
);

CREATE TABLE Produc_comun(
	id_produc_comun serial PRIMARY KEY,
	productos_fk int NOT NULL,
	comunidad_fk int NOT NULL,
	FOREIGN KEY(productos_fk) REFERENCES Productos(id_productos),
	FOREIGN KEY(comunidad_fk) REFERENCES Comunidades(id_comunidades)
);