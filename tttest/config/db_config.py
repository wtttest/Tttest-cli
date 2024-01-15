import peewee
from importlib import import_module

def init_db(project_name):

    cfg = import_module(f'{project_name}.config.cfg')
    get = getattr(cfg, 'get')

    db_info = get('mysql')

    db = peewee.MySQLDatabase(db_info.get('db'), user=db_info.get('user'), password=db_info.get('password'),
                              host=db_info.get('host'), port=db_info.get('port'))
    return db


