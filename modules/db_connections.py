import sqlalchemy
from sqlalchemy import create_engine

def get_mysql_engine(user, password, host, port, database):
    """
    Create a MySQL engine.
    """
    return create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
