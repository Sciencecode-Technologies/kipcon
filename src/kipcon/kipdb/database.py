from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
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

    def getEngine(self):
        return self.__ENGINE
