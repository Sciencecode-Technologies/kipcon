from sqlalchemy import MetaData, Table, Column, Integer, String


class KipTables:
    def __init__(self):
        self.table_names: list = [
            "clients",
            "conf_types",
            "config_files",
            "transactions"
        ]

        self.consts: list = [
            "CONST_FOLDERS",
            "CONST_TOKENS"
        ]

    def CONSTS(self):
        pass