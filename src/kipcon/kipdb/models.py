from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class CONST_FOLDERS(Base):
    __tablename__ = "CONST_FOLDERS"
    CONST_FOLDER_ID: Column = Column('CONST_FOLDER_ID', Integer, primary_key = True)
    main_folder_name: Column = Column('main_folder_name', String(18), nullable = False)
    main_folder_path: Column = Column('main_folder_path', String, nullable = False, unique = False)
    json_folder_name: Column = Column('json_folder_name', String(18), nullable = False)
    ini_folder_name: Column = Column('ini_folder_name', String(18), nullable = False)
    yaml_folder_name: Column = Column('yaml_folder_name', String(18), nullable = False)
    
class Clients(Base):
    __tablename__ = "Clients"
    cl_id = Column(Integer, primary_key = True, nullable = False)
    cl_name: Column = Column(String(18), unique = True, nullable = False)
    cl_ip: Column = Column(String(15), unique = True, nullable = False)
    cl_permissions: Column = Column(String, nullable = False)

class CONST_TOKENS(Base):
    __tablename__ = "CONST_TOKENS"
    token_id: Column = Column('token_id', Integer, primary_key = True)
    token: Column = Column('token', String, unique = True, nullable = False)
    token_creation_datetime: Column = Column('token_creation_datetime', DateTime, default = datetime.now())
    token_update_datetime: Column = Column('token_update_datetime', DateTime, default = datetime.now(), onupdate = datetime.now())
    cl_id: Column = Column(Integer, ForeignKey(Clients.cl_id))

class Conf_types(Base):
    __tablename__ = "Conf_types"
    conf_id: Column = Column(Integer, primary_key = True)
    conf_type: Column = Column(String(8), unique = True, nullable = False)

def make(ENGINE: engine = None):
    Base.metadata.create_all(ENGINE) 