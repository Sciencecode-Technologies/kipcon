from kipcon.kipdb.models import CONST_FOLDERS
from sqlalchemy import update


def const_folders(**kwargs):
    # no need index (id) input
    # const tables must have max one record
    # dont insert, dont delete just update
    def inner(func):
        new_value = func()
        # UPDATE CODE ...
        return True # or new_value
    return inner