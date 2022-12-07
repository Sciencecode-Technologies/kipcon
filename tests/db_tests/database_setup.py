from kipcon.kipdb import *

if __name__ == "__main__":
        # Creating Database
        db = Create_Database()
        # Creating Tables
        make(db.getEngine())

        cfo = CONST_FOLDERS(
                main_folder_name="config_folders",
                main_folder_path="/",
                json_folder_name="json_",
                ini_folder_name="ini_",
                yaml_folder_name="yaml_"
        )

        # level 1 configuration table creating

        db.make_configuration(cfo)

        #db.session.add(cfo) # add row to database
        #db.session.commit() # commit to database

        # do not add any more rows after adding the first row
        # this code must run one time

        # database configuration folder structure builded in kipdb folder
        # all in local folders

        # finally database created (kipcon_main.db)

        db.create_folder_structure()
