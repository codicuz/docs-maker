from docs_maker.database.base import IBase
from docs_maker.database.models import Documents

class InitDb():
    def init(self):
        iBase = IBase()
        engine = iBase.get_sqlite_engine('example.db')
        iBase.Base.metadata.create_all(engine)
        session = iBase.get_session(engine)

        # nd = Documents(name='Doc', date=1)
        # session.add(nd)
        # session.commit()

        session.close()




