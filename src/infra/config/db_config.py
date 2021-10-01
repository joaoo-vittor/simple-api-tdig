from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.session: Session = None

    def get_engine(self) -> Engine:
        """Return connection Engine
        :param - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exe_type, exe_val, exc_tb):
        self.session.close()  # pylint: disable-no-menber