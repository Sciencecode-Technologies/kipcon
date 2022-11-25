from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from kipcon.kipdb.models import CONST_FOLDERS, Conf_types
import os


class Create_Database:
    def __init__(self, db_path: str=os.path.dirname(__file__), db_name: str="kipcon_main.db"):
        self.__ENGINE = create_engine('sqlite:///'+db_path+'/'+db_name, echo=True)

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
