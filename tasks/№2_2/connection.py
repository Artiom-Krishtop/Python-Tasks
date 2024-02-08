from engine import Engine

class Connection():

    def __init__(self, engine: Engine):
        self._engine = engine

    def get_connection(self):
        with self._engine.connect() as conn:
            return conn      
