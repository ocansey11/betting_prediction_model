import sqlalchemy
from sqlalchemy import create_engine

def get_mysql_engine(user, password, host, port, database):
    """
    Create a MySQL engine. If the password is None or an empty string, it omits it from the connection string.
    """
    if password:
        connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    else:
        connection_string = f'mysql+pymysql://{user}@{host}:{port}/{database}'
    
    return create_engine(connection_string)