create database Inventi;

USE Inventi;

CREATE TABLE USUARIO(
	id_usuario INT auto_increment primary key,
    nombre VARCHAR(50),
    password VARCHAR(250),
    email VARCHAR(100) UNIQUE,
    id_rol INT NOT NULL,
    -- Clave foránea que enlaza USER con ROLES
    FOREIGN KEY (id_rol) REFERENCES ROLES(id_rol)
);

CREATE TABLE ROLES(
    id_rol INT auto_increment primary key,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE PRODUCTOS(
    id_producto INT PRIMARY KEY auto_increment,
    nombre VARCHAR(50),
    descripcion TEXT,
    precio_venta DECIMAL(10, 2),
    id_categoria INT NOT NULL,
	activo BOOLEAN NOT NULL DEFAULT TRUE, -- Por defecto, el producto está activo
    fecha_vencimiento DATE NULL, 
    -- Restricción CHECK: El precio de venta debe ser positivo
    CHECK (precio_venta >= 0),
    -- Clave foránea que enlaza PRODUCTOS con CATEGORIAS
    FOREIGN KEY (id_categoria) REFERENCES CATEGORIAS(id_categorias)
);

CREATE TABLE CATEGORIAS(
    id_categorias INT PRIMARY KEY auto_increment,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE INVENTARIO(
    INT PRIMARY KEY auto_increment,
    id_productos INT NOT NULL UNIQUE,
    stock_actual INT NOT NULL,
    stock_minimo INT NOT NULL,
    fecha_ultima_entrada DATETIME NOT NULL,
    -- Restricción CHECK: El stock no puede ser negativo
    CHECK (stock_actual >= 0),
    CHECK (stock_minimo >= 0),
    CONSTRAINT chk_stock_minimo CHECK (stock_actual >= stock_minimo),
    -- Clave foránea que enlaza INVENTARIO con PRODUCTOS
    FOREIGN KEY (id_productos) REFERENCES PRODUCTOS(id_producto)
);

##Datos para la DB
-- Insertar ROLES
INSERT INTO ROLES (id_rol, nombre_rol) VALUES
(1, 'Administrador'),
(2, 'Vendedor'),
(3, 'Almacenista');

-- Insertar CATEGORIAS
INSERT INTO CATEGORIAS (nombre) VALUES
('Electrónica'),
('Lacteos'),
('Frutas'),
('Enlatados'),
('Bebidas'),
('Hogar'),
('Snack'),
('Alimentos'),
('Higiene');

-- Insertar USER (necesitan un id_rol existente)
INSERT INTO USER (nombre, password_hash, email, id_rol) VALUES
('Ana Perez', 'hash123adm', 'ana.perez@inventi2.com', 1), -- Administrador
('Carlos V', 'hash456ven', 'carlos.v@inventi2.com', 2),  -- Vendedor
('Luisa M', 'hash789alm', 'luisa.m@inventi2.com', 3);   -- Almacenista

-- Insertar PRODUCTOS (necesitan un id_categoria existente)
INSERT INTO PRODUCTOS (nombre, descripcion, precio_venta, id_categoria, activo) VALUES
('Monitor Curvo 27"', 'Monitor para gaming y diseño', 350.50, 1, TRUE),
('Silla Ergonómica', 'Silla de oficina ajustable', 120.00, 1, TRUE),
('Cafetera Programable', 'Cafetera automática con timer', 45.99, 2, TRUE),
('Teclado Mecánico', 'Teclado RGB con switches azules', 75.00, 1, TRUE),
('Papel Bond A4', 'Paquete de 500 hojas', 5.50, 6, FALSE), -- Producto inactivo
('Tostadora', 'Tostadora de 2 rebanadas', 25.00, 6, TRUE);

-- Insertar INVENTARIO (necesitan un id_producto existente)
INSERT INTO INVENTARIO (id_productos, stock_actual, stock_minimo, fecha_ultima_entrada) VALUES
(1, 15, 5, '2025-11-20 10:00:00'),
(2, 50, 10, '2025-12-01 15:30:00'),
(3, 30, 8, '2025-11-25 09:00:00'),
(4, 5, 5, '2025-12-01 18:00:00'),
(6, 40, 12, '2025-10-15 11:00:00');

SELECT  * FROM PRODUCTOS;

##Inserción, Actualización y Eliminación
###Insercion
-- 1. Inserción del nuevo producto
INSERT INTO PRODUCTOS (nombre, descripcion, precio_venta, id_categoria, activo) VALUES
('Barra de Cereal', 'Caja de 12 barras energéticas', 12.99, 4, TRUE);

-- 2. Inserción de su inventario (asumimos que la barra de cereal es el id_producto 7)
INSERT INTO INVENTARIO (id_productos, stock_actual, stock_minimo, fecha_ultima_entrada) VALUES
(LAST_INSERT_ID(), 100, 20, NOW()); -- LAST_INSERT_ID() obtiene el id_producto generado en la inserción anterior

##UPDATE
UPDATE PRODUCTOS
SET precio_venta = precio_venta * 1.10 -- Operación matemática
WHERE id_categoria = 1;

-- Luego se actualiza la tabla de Inventario para reflejar que se recibió mercancía del producto 4 (Teclado Mecánico)
UPDATE INVENTARIO
SET stock_actual = stock_actual + 20,
    fecha_ultima_entrada = NOW()
WHERE id_productoS = 4;

##DELETE
-- Para el ejemplo del "Papel Bond A4" (id_producto 5), no tiene inventario, así que se puede eliminar.
DELETE FROM PRODUCTOS
WHERE id_producto = 5 AND activo = FALSE;

##PRUEBAS (JOINS)

SELECT
    C.nombre AS Categoria,
    COUNT(P.id_producto) AS Num_Producto,
    ROUND(SUM(I.stock_actual * P.precio_venta), 2) AS Valor_Total_Inventario_USD,
    U.nombre AS Administrador_Responsable
FROM
    PRODUCTOS P
INNER JOIN CATEGORIAS C ON P.id_categoria = C.id_categorias
INNER JOIN INVENTARIO I ON P.id_producto = I.id_productos -- ¡USO DEL PLURAL!
INNER JOIN USER U ON U.id_rol = 1
WHERE
    P.activo = TRUE
GROUP BY
    C.nombre, U.nombre
ORDER BY
    Valor_Total_Inventario_USD DESC;
    




DELETE FROM Usuarios WHERE id_usuario = 2;
alter table Usuarios auto_increment = 1;

ALTER TABLE PRODUCTOS ADD COLUMN fecha_vencimiento DATE;
