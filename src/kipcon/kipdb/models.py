from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import engine, update
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class CONST_FOLDERS(Base):
    __tablename__ = "CONST_FOLDERS"
    CONST_FOLDER_ID: Column = Column('CONST_FOLDER_ID', Integer, primary_key = True, autoincrement=True)
    main_folder_name: Column = Column('main_folder_name', String(18), nullable = False)
    main_folder_path: Column = Column('main_folder_path', String, nullable = False, unique = False)
    json_folder_name: Column = Column('json_folder_name', String(18), nullable = False)
    ini_folder_name: Column = Column('ini_folder_name', String(18), nullable = False)
    yaml_folder_name: Column = Column('yaml_folder_name', String(18), nullable = False)

class Clients(Base):
    __tablename__ = "Clients"
    cl_id = Column(Integer, primary_key = True, nullable = False, autoincrement=True)
    cl_name: Column = Column(String(18), unique = True, nullable = False)
    cl_ip: Column = Column(String(15), unique = True, nullable = False)
    cl_permissions: Column = Column(String, nullable = False)

class CONST_TOKENS(Base):
    __tablename__ = "CONST_TOKENS"
    token_id: Column = Column('token_id', Integer, primary_key = True, autoincrement=True)
    token: Column = Column('token', String, unique = True, nullable = False)
    token_creation_datetime: Column = Column('token_creation_datetime', DateTime, default = datetime.now())
    token_update_datetime: Column = Column('token_update_datetime', DateTime, default = datetime.now(), onupdate = datetime.now())
    cl_id: Column = Column(Integer, ForeignKey(Clients.cl_id))

class Conf_types(Base):
    __tablename__ = "Conf_types"
    conf_id: Column = Column(Integer, primary_key = True, autoincrement=True)
    conf_type: Column = Column(String(8), unique = True, nullable = False)

class Config_files(Base):
    __tablename__ = "Config_files"
    configfile_id: Column = Column(Integer, primary_key = True, autoincrement=True)
    conf_type: Column = Column(Integer, ForeignKey(Conf_types.conf_type), nullable = False)
    configfile_name: Column = Column(String(18), nullable = False)
    configfile_folder_id: Column = Column(Integer, ForeignKey(CONST_FOLDERS.CONST_FOLDER_ID), nullable = False)
    configfile_creation_datetiöe: Column = Column(DateTime, default = datetime.now(), nullable = False)
    configfile_update_time: Column = Column(DateTime, default = datetime.now(), onupdate = datetime.now(), nullable = False)
    configfile_status: Column = Column(Integer, nullable = False)
    configfile_special_code: Column = Column(String, unique = True, nullable = False)

class Transactions(Base):
    __tablename__ = "Transactions"
    tn_id: Column = Column(Integer, primary_key = True, autoincrement=True)
    tn_token_id: Column = Column(Integer, ForeignKey(CONST_TOKENS.token_id), nullable = False)
    tn_datetime: Column = Column(DateTime, nullable = False, default = datetime.now())
    tn_configfile_id: Column = Column(Integer, ForeignKey(Config_files.configfile_id), nullable = False)
    tn_status: Column(Integer, nullable = False)

def make(ENGINE: engine = None):
    Base.metadata.create_all(ENGINE)
