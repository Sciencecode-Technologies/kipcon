from kipcon.kipdb.database_actions import *
from kipcon.kipdb.models import *
from sqlalchemy import engine


if __name__ == "__main__":

    @const_folders(column = "main_folder_name") # import COLUMN type
    def update(value = "main2"):
        return value

    # const tokens . . .
    # creation   

    print(update)
