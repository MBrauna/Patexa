import logging
from ..gateway.DatabaseGateway import DatabaseGateway

class MysqlDB(DatabaseGateway):
    __type = "mysql+pymysql"

    def __init__(self, config: dict):
        try:
            super(MysqlDB, self).__init__()
            logging.info(f"[MysqlDB] creating database {config['host']}")
            tmp_url = f"{self.__type}://{config['username']}:{config['password']}@" \
                      f"{config['host']}:{config['port']}/{config['database']}"
            self.init_database(tmp_url)
        except Exception as error:
            logging.error(f"[{self.__type}] error when generate DB - {error}")

    def engineClose(self) -> None:
        try:
            logging.info(f"[{self.__type}] closing sessions and database from {self.__type}")
            super(MysqlDB, self).engineClose()
            self.close_connection()
            logging.info(f"[{self.__type}] Success clossing connection {self.__type}")
        except Exception as error:
            logging.error(f"[{self.__type}] error when generate DB")
