from engine import Engine
from sqlalchemy.orm import sessionmaker 

class Session():

    def __init__(self, engine: Engine):
        self._session = sessionmaker(bind=engine)

    def get_session(self):
        with self._session() as session:
            return session      
