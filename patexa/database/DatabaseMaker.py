import logging
from .plugin.PostgresDB import PostgresDB
from .plugin.MysqlDB import MysqlDB
from .plugin.SqliteDB import SqliteDB


class DatabaseMaker:
    def create_configuration(self, config: dict):
        match config['type'].lower():
            case 'postgres':
                return PostgresDB(config)
            case 'mysql':
                return MysqlDB(config)
            case 'sqlite':
                return SqliteDB(config)
            case _:
                Exception(f"[Database Maker]Cannot find driver to {config['type']}")
