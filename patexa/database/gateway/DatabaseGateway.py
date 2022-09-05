import logging

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker, Session


class DatabaseGateway:
    # --------------------------------- #
    connection: Engine = None
    connection_url: str = None
    session: Session = None

    # --------------------------------- #
    def init_database(self, url: str) -> None:
        if url is None:
            Exception(f"[__initDatabase] url is required")
        self.connection_url = url
        self.connection = create_engine(self.connection_url)
        session_created = sessionmaker(bind=self.connection)
        self.session = session_created()
        logging.info(f"[__initDatabase] Connection and Session was created by engine generator")

    def close_connection(self) -> None:
        if self.session.is_active:
            self.session.close_all()
            self.connection.clear_compiled_cache()
        self.session = None
        self.connection = None
        self.connection_url = None
