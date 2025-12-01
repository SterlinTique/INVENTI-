import os # importa el modulo estandar de Python para trabajar con el sistema operativo 

basedir = os.path.abspath(os.path.dirname(__file__)) # obtiene la ruta absoluta del directorio actual

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:password@localhost/contenedor1'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
