from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


class Rol(db.Model):
    __tablename__ = 'ROLES'
    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_rol = db.Column(db.String(50), unique=True, nullable=False)

    usuarios = db.relationship('Usuario', backref='rol', lazy=True)

    def __repr__(self):
        return f'<Rol {self.nombre_rol}>'


class Usuario(db.Model):
    __tablename__ = 'USUARIOS'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(250), nullable=False) # contra hasheada
    email = db.Column(db.String(100), unique=True, nullable=False)
    id_rol = db.Column(db.Integer, db.ForeignKey('ROLES.id_rol'), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.email}>'


class Categoria(db.Model):
    __tablename__ = 'CATEGORIAS'
    id_categorias = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    productos = db.relationship('Producto', backref='categoria', lazy=True)

    def __repr__(self):
        return f'<Categoria {self.nombre}>'


class Producto(db.Model):
    __tablename__ = 'PRODUCTOS'
    id_producto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    precio_venta = db.Column(db.Numeric(10, 2), nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('CATEGORIAS.id_categorias'), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)    
    fecha_vencimiento = db.Column(db.Date, nullable=True)

    inventario = db.relationship('Inventario', backref='producto', uselist=False)

    def __repr__(self):
        return f'<Producto {self.nombre} - ${self.precio_venta}>'
    

class Inventario(db.Model):
    __tablename__ = 'INVENTARIO'
    id_inventario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_productos = db.Column(db.Integer, db.ForeignKey('PRODUCTOS.id_producto'), unique=True, nullable=False)
    stock_actual = db.Column(db.Integer, nullable=False)
    stock_minimo = db.Column(db.Integer, nullable=False)
    fecha_ultima_entrada = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Inventario ProductoID={self.id_productos} Stock={self.stock_actual}>'