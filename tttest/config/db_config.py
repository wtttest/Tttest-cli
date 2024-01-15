import peewee
from importlib import import_module

from tttest.utils.utils import get


def init_db(db_config_path):
    db_info = get(key='mysql', config_path=db_config_path)

    db = peewee.MySQLDatabase(db_info.get('db'), user=db_info.get('user'), password=db_info.get('password'),
                              host=db_info.get('host'), port=db_info.get('port'))
    return db
