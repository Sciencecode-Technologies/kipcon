from kipcon.kipdb import *

if __name__ == "__main__":
        db = Create_Database()
        make(db.getEngine())

        cfo = CONST_FOLDERS(
                main_folder_name="config_folders",
                main_folder_path="/",
                json_folder_name="json_",
                ini_folder_name="ini_",
                yaml_folder_name="yaml_"
        )

        db.session.add(cfo) # add row to database
        db.session.commit() # commit to database

        # do not add any more rows after adding the first row