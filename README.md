# Proyecto de Login y CRUD con Flask y MySQL

Este proyecto fue desarrollado con el objetivo de aplicar conceptos claves y modularidad; y ahora utilizado en el curso Base de Datos. La aplicación incluye un sistema de login/registro (con hasheo de contraseñas) y un CRUD para gestionar productos, con arquitectura desacoplada entre frontend y backend.

##  Arquitectura

- **Frontend**: HTML, CSS y JavaScript estáticos, desacoplados del backend.
- **Backend**: API REST construida con Flask, conectada a MySQL.
- **Base de datos**: MySQL.

## Tecnologías y herramientas utilizadas

| Categoría             | Herramientas / Tecnologías                            |
|-----------------------|-------------------------------------------------------|
| Lenguajes             | Python 3.11, HTML, CSS, JavaScript                    |
| Frameworks            | Flask (microframework para backend web/API)           |
| Base de datos         | MySQL                                                 |
| Seguridad             | Werkzeug (hash de contraseñas), dotenv (variables de entorno) |
| Control de versiones  | Git, GitHub                                           |
| Editor sugerido       | Visual Studio Code                                    |


## Estructura del proyecto
```plaintext
├── backend/ 
│ ├── app.py 
│ ├── config.py 
│ ├── basededatos.py 
│ ├── conexion.py 
│ └── requirements.txt 
├── frontend/ 
│ ├── index.html 
│ ├── dashboard.html 
│ ├── loginRegistro.html 
│ ├── productos/ 
│ │ ├── crear.html 
│ │ ├── editar.html 
│ │ └── listar.html 
│ ├── css/ 
│ │ └── estilos.css 
│ └── js/ 
│ │ ├── api.js 
│ │ ├── dashboard.js 
│ │ ├── loginRegistro.js 
│ │ ├── index.js 
│ │ ├── crear.js 
│ │ ├── listar.js 
│ │ └── editar.js
```

## Funcionalidades

- Registro y login de usuarios con contraseña encriptada
- CRUD completo de productos (crear, listar, editar, eliminar)
- API REST con respuestas en JSON
- Frontend desacoplado que consume la API vía `fetch()`
- Contenedores Docker para backend y base de datos


## Instalación

###

1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv env`
3. Activa el entorno: `source env/bin/activate` (Linux/macOS) o `.\env\Scripts\activate` (Windows)
4. Instala dependencias: `pip install -r requirements.txt` o `python -m pip install -r requirements.txt`
5. Confirma la instalación de las dependencias en el entorno virtual `python -m pip list`
6. Configura la conexión a MySQL en `config.py` 
7. Ejecuta el backend: `python app.py`
8. Abre `frontend/login.html` directamente en tu navegador.


## Uso

1. Abre `frontend/login.html` en tu navegador.
2. Regístrate y accede con tus credenciales.
3. Navega entre las páginas para listar, crear, editar o eliminar productos.
4. El frontend se comunica con el backend vía API REST.

## Notas

- Si `pip` lanza errores, ejecuta: `pip install --upgrade setuptools`

---

| Paquete               | Descripción                                                                   |
|-----------------------|-------------------------------------------------------------------------------|
| `Flask`               | Microframework para construir aplicaciones web y APIs REST en Python.         |
| `Flask-Bcrypt`        | Integra `bcrypt` con Flask para hashear contraseñas de forma segura.          |
| `Flask-Login`         | Maneja sesiones de usuario, login/logout y protección de rutas.               |
| `Flask-SQLAlchemy`    | ORM que conecta Flask con bases de datos relacionales como PostgreSQL.        |
| `Flask-WTF`           | Integra formularios HTML con validación en Flask usando WTForms.              |
| `Flask-Cors`          | Permite que el frontend desacoplado consuma la API desde otro dominio.        |
| `Werkzeug`            | Biblioteca base de Flask para enrutamiento, servidor y seguridad HTTP.        |
| `Jinja2`              | Motor de plantillas usado por Flask (aunque no se usa en frontend desacoplado)|
| `WTForms`             | Permite definir y validar formularios HTML en Python.                         |
| `bcrypt`              | Algoritmo de cifrado para generar/verificar hashes de contraseñas.            |
| `PyMySQL`     | Driver que permite a Python conectarse a bases de datos MySQL.           |
| `SQLAlchemy`          | ORM que traduce modelos Python a SQL y gestiona consultas.                    |
| `greenlet`            | Biblioteca de concurrencia ligera usada por SQLAlchemy.                       |
| `itsdangerous`        | Genera tokens seguros para sesiones o recuperación de contraseña.             |
| `blinker`             | Sistema de señales usado por Flask para emitir eventos internos.              |
| `click`               | Utilidad para crear comandos en la terminal (usado por Flask CLI).            |
| `colorama`            | Permite imprimir texto con colores en la terminal (útil para depuración).     |
| `MarkupSafe`          | Protege contra inyecciones de HTML/JS al escapar contenido en plantillas.     |
| `typing_extensions`   | Proporciona tipos adicionales para anotaciones en Python.                     |
| `python-dotenv`       | Permite cargar variables de entorno desde un archivo `.env`.                  |
