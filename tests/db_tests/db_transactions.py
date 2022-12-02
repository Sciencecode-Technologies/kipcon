from kipcon.kipdb.database_actions import *


if __name__ == "__main__":

    @const_folders(column = "main_folder_name")
    def update(value = "main2"):
        return value
    
    print(update)