from kipcon.kipdb import *
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
        ENGINE = Create_Database().getEngine()
        make(ENGINE)

        session = sessionmaker(bind = ENGINE)

        c = Conf_types()
        c.insert().values(conf_type = "ini")

        session.add(c)
        session.commit()