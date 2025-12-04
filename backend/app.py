from flask import Flask, request, jsonify # Importar Flask y módulos necesarios
from flask_sqlalchemy import SQLAlchemy # Importar SQLAlchemy para la base de datos
from flask_cors import CORS # Importar CORS para manejar solicitudes de diferentes orígenes
from werkzeug.security import generate_password_hash, check_password_hash # Importar funciones de seguridad para manejo de contraseñas
from dotenv import load_dotenv
from config import Config   # Importar configuración desde el archivo config.py
from basededatos import db, init_app, Usuario, Producto, Categoria, Inventario, Rol# Importar la base de datos y modelos desde basededatos.py

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__) # Inicializar la aplicación Flask
app.config.from_object(Config) # Cargar configuración desde el objeto Config
init_app(app) # Inicializar la base de datos con la aplicación Flask
CORS(app) # Habilitar CORS para la aplicación

with app.app_context(): # Probar la conexión a la base de datos
    try: # Uso de try-except para manejar errores
        db.engine.connect() # Intentar conectar a la base de datos
        print("Conexión a la base de datos exitosa") 
    except Exception as e: 
        print("Error al conectar a la base de datos: ", e)

# Login
@app.route('/api/login', methods=['POST']) # Ruta para el login
def api_login(): 
    data = request.get_json() # Obtener datos JSON del request
    email = data.get('email') # Obtener el email
    password = data.get('password') # Obtener la contraseña
    usuario = Usuario.query.filter_by(email=email).first() # Buscar el email en la base de datos
    # Verificar la contraseña
    if usuario and check_password_hash(usuario.password, password): # Si la contraseña es correcta
        return jsonify({"success": True, "message": "Login correcto", "rol": usuario.rol.nombre_rol}), 200 # Devolver respuesta exitosa mediante un 200 y el rol del usuario
    return jsonify({"success": False, "message": "Login incorrecto"}), 401 # Devolver respuesta de error mediante un 401

# Registro
@app.route('/api/registro', methods=['POST'])
def api_registro():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    password = data.get('password')
    confirmar_password = data.get('confirmarContraseña')

    # para validar que las contraseñas coincidan
    if password != confirmar_password:
        return jsonify({"success": False, "message": "Las contraseñas no coinciden"}), 400
    # para validar que el email no este ya registrado
    if Usuario.query.filter_by(email=email).first(): # el first sirve para obtener el primer resultado o None si no existe
        return jsonify({"success": False, "message": "El correo ya está registrado"}), 400

    hashed_password = generate_password_hash(password) # despues de confirmar la contra ahora si se hashea 
    usuario = Usuario(nombre=nombre, password=hashed_password, email=email, id_rol=2) # crea nuevo usuario
    db.session.add(usuario) # agrega a la sesion
    db.session.commit() # guarda en la base de datos
    return jsonify({"success": True, "message": "Usuario registrado"}), 201 

# Listar productos
@app.route('/api/productos', methods=['GET'])
def api_listar_productos():
    productos = Producto.query.all() # obtener todos los productos
    resultado = [
        {"id": p.id_producto, "nombre": p.nombre, "descripcion": p.descripcion, "precio": p.precio_venta, "activo": p.activo, "fecha_vencimiento": p.fecha_vencimiento.isoformat() if p.fecha_vencimiento else None, 'categoria': p.categoria.nombre
        }
        for p in productos
    ]
    return jsonify(resultado), 200

# Crear producto
@app.route('/api/productos', methods=['POST'])
def api_crear_producto():
    data = request.get_json()
    producto = Producto(
        nombre=data.get('nombre'),
        descripcion=data.get('descripcion'),
        precio_venta=data.get('precio_venta'),
        fecha_vencimiento=data.get('fecha_vencimiento'),
        id_categoria=data.get('id_categoria'),
        activo=True
    )
    db.session.add(producto)
    db.session.commit()
    return jsonify({"success": True, "message": "Producto creado"}), 201

# Editar producto
@app.route('/api/productos/<int:id>', methods=['PUT'])
def api_editar_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"success": False, "message": "Producto no encontrado"}), 404
    
    data = request.get_json()
    producto.nombre = data.get('nombre')
    producto.descripcion = data.get('descripcion')
    producto.precio_venta = data.get('precio_venta')
    producto.fecha_vencimiento = data.get('fecha_vencimiento')
    producto.id_categoria = data.get('id_categoria')
    db.session.commit()
    return jsonify({"success": True, "message": "Producto actualizado"}), 200

# Eliminar producto
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def api_eliminar_producto(id):
    producto = Producto.query.get(id) 
    
    if not producto: # si el producto no existe
        return jsonify({"success": False, "message": "Producto no encontrado"}), 404
    
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"success": True, "message": "Producto eliminado"}), 200


# Listar inventario
@app.route('/api/inventario', methods=['GET'])
def api_listar_inventario():
    inventarios = Inventario.query.all()
    resultado = [
        {
            "id_inventario": i.id_inventario,
            "producto": i.producto.nombre,
            "stock_actual": i.stock_actual,
            "stock_minimo": i.stock_minimo,
            "fecha_ultima_entrada": i.fecha_ultima_entrada.isoformat()
        }
        for i in inventarios
    ]
    return jsonify(resultado), 200


# Actualizar inventario
@app.route('/api/inventario/<int:id>', methods=['PUT'])
def api_actualizar_inventario(id):
    inventario = Inventario.query.get(id)
    if not inventario:
        return jsonify({"success": False, "message": "Inventario no encontrado"}), 404

    data = request.get_json()
    inventario.stock_actual = data.get('stock_actual', inventario.stock_actual)
    inventario.stock_minimo = data.get('stock_minimo', inventario.stock_minimo)
    inventario.fecha_ultima_entrada = data.get('fecha_ultima_entrada', inventario.fecha_ultima_entrada)

    db.session.commit()
    return jsonify({"success": True, "message": "Inventario actualizado"}), 200



# Alertas de inventario bajo
@app.route('/api/inventario/alertas', methods=['GET'])
def api_alertas_inventario():
    alertas = Inventario.query.filter(Inventario.stock_actual < Inventario.stock_minimo).all()
    resultado = [
        {
            "producto": i.producto.nombre,
            "stock_actual": i.stock_actual,
            "stock_minimo": i.stock_minimo
        }
        for i in alertas
    ]
    return jsonify({"success": True, "alertas": resultado}), 200

# Crear inventario cuando se añade un nuevo producto
@app.route('/api/inventario', methods=['POST'])
def api_crear_inventario():
    data = request.get_json()
    inventario = Inventario(
        id_productos=data.get('id_productos'),
        stock_actual=data.get('stock_actual'),
        stock_minimo=data.get('stock_minimo'),
        fecha_ultima_entrada=data.get('fecha_ultima_entrada')
    )
    db.session.add(inventario)
    db.session.commit()
    return jsonify({"success": True, "message": "Inventario creado"}), 201


# Reporte convinado y general de productos con inventario
@app.route('/api/reporte', methods=['GET'])
def api_reporte_general():
    productos = Producto.query.join(Categoria).outerjoin(Inventario).all()
    resultado = [
        {
            "id_producto": p.id_producto,
            "nombre": p.nombre,
            "descripcion": p.descripcion,
            "precio_venta": str(p.precio_venta),
            "activo": p.activo,
            "fecha_vencimiento": p.fecha_vencimiento.isoformat() if p.fecha_vencimiento else None,
            "categoria": p.categoria.nombre,
            "inventario": {
                "stock_actual": p.inventario.stock_actual if p.inventario else None,
                "stock_minimo": p.inventario.stock_minimo if p.inventario else None,
                "fecha_ultima_entrada": p.inventario.fecha_ultima_entrada.isoformat() if p.inventario else None,
                "alerta_stock_bajo": (
                    p.inventario.stock_actual < p.inventario.stock_minimo
                    if p.inventario else False
                )
            }
        }
        for p in productos
    ]
    return jsonify({"success": True, "data": resultado}), 200


# Reporte resumido por categoría
@app.route('/api/reporte/categorias', methods=['GET'])
def api_reporte_categorias():
    # Agrupar productos por categoría y calcular estadísticas
    categorias = Categoria.query.all()
    resultado = []

    for c in categorias:
        productos = Producto.query.filter_by(id_categoria=c.id_categorias, activo=True).all()
        total_productos = len(productos)
        valor_total = 0
        stock_total = 0

        for p in productos:
            if p.inventario:
                valor_total += float(p.inventario.stock_actual) * float(p.precio_venta)
                stock_total += p.inventario.stock_actual

        resultado.append({
            "categoria": c.nombre,
            "total_productos_activos": total_productos,
            "stock_total": stock_total,
            "valor_total_inventario": round(valor_total, 2)
        })

    return jsonify({"success": True, "data": resultado}), 200


if __name__ == '__main__': # ejecuta la aplicación Flask
    app.run(debug=True)