from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from kipcon.kipdb.models import CONST_FOLDERS, Conf_types
import os


class Create_Database:
    def __init__(self, db_path: str=os.path.dirname(__file__), db_name: str="kipcon_main.db"):
        self.__ENGINE = create_engine('sqlite:///'+db_path+'/'+db_name, echo=True)
        
        self.db_path = db_path

        if not database_exists(self.__ENGINE.url):
            create_database(self.__ENGINE.url)
            # tablolarda meta_Create_kullanılacak
            # create tables gibi bir fonksiyon

        self.Session = sessionmaker(bind = self.__ENGINE)
        self.session = self.Session()

    def make_configuration(self, config_folders_table: CONST_FOLDERS):
        flag = False
        conn = self.__ENGINE.connect()
        result = conn.execute(select(CONST_FOLDERS))
        self.cfo = config_folders_table

        if result.fetchone() == None:
            # checks if configuration data is saved in database
            self.session.add(config_folders_table)

            for typ in ["ini", "conf", "yaml", "json"]:
                self.session.add(Conf_types(conf_type=typ))

            self.session.commit()
            flag = True

        return flag

    def getEngine(self):
        return self.__ENGINE

    def create_folder_structure(self):
        flag = False
        if self.cfo.main_folder_name not in os.listdir(self.db_path):
            os.mkdir(self.db_path+"/"+self.cfo.main_folder_name)
            os.mkdir(self.db_path+"/"+self.cfo.main_folder_name+"/"+self.cfo.ini_folder_name)
            os.mkdir(self.db_path+"/"+self.cfo.main_folder_name+"/"+self.cfo.json_folder_name)
            os.mkdir(self.db_path+"/"+self.cfo.main_folder_name+"/"+self.cfo.yaml_folder_name)
            flag = True

        return flag


class Database_Transactions:
    #change const_folders
    class const_folders(CONST_FOLDERS):
        
        def main_folder_name(self):
            def change():
                pass
            

class User_Transactions:
    pass