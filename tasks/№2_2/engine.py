from sqlalchemy import create_engine

class Engine():

    def __init__(self, url):
        self._url = url

    def create_engine(self):
        return create_engine(self._url)