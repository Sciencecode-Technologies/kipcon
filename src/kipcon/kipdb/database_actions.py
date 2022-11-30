from kipcon.kipdb.models import CONST_FOLDERS
from sqlalchemy import update


def const_folders(**kwargs):
    def inner(func):
        new_value = func()
        # UPDATE CODE ...
        return True # or new_value
    return inner