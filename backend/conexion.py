import os
from sqlalchemy import create_engine

def conectar():
    database_url = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:password@localhost/contenedor1'
    )
    engine = create_engine(database_url)
    return engine
