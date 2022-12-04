from kipcon.kipdb.models import CONST_FOLDERS
from kipcon.kipdb.database import Create_Database
from sqlalchemy import update, select, column, engine


def const_folders(**kwargs):
    # no need index (id) input
    # const tables must have max one record
    # dont insert, dont delete just update
    def inner(func):
        new_value = func()
        #s = select(column(kwargs['column']))
        #r = connection.execute(s).fetchall()
        return True # or new_value
    return inner