import logging
from ..gateway.DatabaseGateway import DatabaseGateway

class SqliteDB(DatabaseGateway):
    __type = "sqlite"

    def __init__(self, config: dict):
        try:
            logging.info(f"[Sqlite] creating database {config['host']}")
            super.__init__(f"{self.__type}:///{config['host']}")

        except Exception as error:
            logging.error(f"[Sqlite] error when generate DB - {error}")

    def engine_close(self) -> None:
        try:
            logging.info(f"[Sqlite] closing sessions and database from {self.__type}")
            super().closeConnection()
            logging.info(f"[Sqlite] Success clossing connection {self.__type}")
        except Exception as error:
            logging.error(f"[Sqlite] error when generate DB {error}")