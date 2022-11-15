from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os


class Create_Database:
    def __init__(self, db_path: str = os.path.dirname(__file__), db_name: str = "kipcon_main.db"):
        self.engine = create_engine('sqlite:///'+db_path+'/'+db_name, echo = True)
        
        if not database_exists(self.engine.url):
            create_database(self.engine.url)

        