from backend.sql_app.config.database import SessionLocal


class BaseDAO():
    _instance = None
    _session = None
    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def conf(self):
        return self.g.conf


    @property
    def session(self):
        if self._session is None:
            self._session = SessionLocal()
        return self._session

