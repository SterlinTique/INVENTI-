from flask import Flask, request, jsonify # Importar Flask y módulos necesarios
from flask_sqlalchemy import SQLAlchemy # Importar SQLAlchemy para la base de datos
from flask_cors import CORS # Importar CORS para manejar solicitudes de diferentes orígenes
from werkzeug.security import generate_password_hash, check_password_hash # Importar funciones de seguridad para manejo de contraseñas
from dotenv import load_dotenv
from config import Config   # Importar configuración desde el archivo config.py
from basededatos import db, init_app, Usuario, Producto # Importar la base de datos y modelos desde basededatos.py

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
    username = data.get('username') # Obtener el nombre de usuario
    password = data.get('password') # Obtener la contraseña
    usuario = Usuario.query.filter_by(username=username).first() # Buscar el usuario en la base de datos
    # Verificar la contraseña
    if usuario and check_password_hash(usuario.password, password): # Si la contraseña es correcta
        return jsonify({"success": True, "message": "Login correcto"}), 200 # Devolver respuesta exitosa mediante un 200
    return jsonify({"success": False, "message": "Login incorrecto"}), 401 # Devolver respuesta de error mediante un 401

# Registro
@app.route('/api/registro', methods=['POST'])
def api_registro():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))  # Hashed password
    email = data.get('email')
    usuario = Usuario(username=username, password=password, email=email)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"success": True, "message": "Usuario registrado"}), 201

# Listar productos
@app.route('/api/productos', methods=['GET'])
def api_listar_productos():
    productos = Producto.query.all()
    resultado = [
        {"id": p.id, "nombre": p.nombre, "descripcion": p.descripcion, "precio": p.precio}
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
        precio=data.get('precio')
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
    producto.precio = data.get('precio')
    db.session.commit()
    return jsonify({"success": True, "message": "Producto actualizado"}), 200

# Eliminar producto
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def api_eliminar_producto(id):
    producto = Producto.query.get(id)
    if not producto:
        return jsonify({"success": False, "message": "Producto no encontrado"}), 404
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"success": True, "message": "Producto eliminado"}), 200

if __name__ == '__main__':
    app.run(debug=True)
