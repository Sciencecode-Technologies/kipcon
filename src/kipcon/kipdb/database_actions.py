from kipcon.kipdb.models import CONST_FOLDERS
from sqlalchemy import update


"""def add_client(func):
    def inner(a):
        return func(a)
    return inner

def add_client2(func):
    def inner():
        return func(3)
    return inner

def add_client3(*args, **kwargs):
    def inner(func):
        print(kwargs['f'])
        func()
    return inner

def addx(**kwargs):
    def inner(func):
        return func(kwargs['x']*2)
    return inner"""
# PRACTICE


def const_folders(**kwargs):
    def inner(func):
        new_value = func()
        # UPDATE CODE ...
        return True # or new_value
    return inner