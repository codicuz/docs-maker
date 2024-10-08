import pytest
from sqlalchemy import inspect
from docs_maker.database.base import IBase
from docs_maker.database.models import Documents
from docs_maker.database.models import Configurations

class TestDocsMaker():
    @pytest.fixture(scope="function")
    def in_memory_db(self):
        iBase = IBase()
        engine = iBase.get_sqlite_engine(':memory:')
        iBase.Base.metadata.create_all(engine)
        session = iBase.get_session(engine)
        
        yield session, engine

        session.close()
        
    def test_documents_table(self, in_memory_db):
        _, engine = in_memory_db
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        table = 'documents'
        assert table in tables, f"Таблица {table} должна быть создана"

        table = 'configurations'
        assert table in tables, f"Таблица {table} должна быть создана"

    def test_insert_documents_table(self, in_memory_db):
        session, _ = in_memory_db

        name = 'Fake Document'
        descr = 'Fake description'
        
        new_doc = Documents(name=name, description=descr)

        session.add(new_doc)
        session.commit()

        inserted_doc = session.query(Documents).filter_by(name=name).first()

        assert inserted_doc is not None, "Документ должен быть вставлен"
        assert inserted_doc.name == name, f"Имя документа должно быть {name}"
        assert inserted_doc.description == descr, f"Описание должно быть {descr}"

    def test_insert_configurations_table(self, in_memory_db):
        session, _ = in_memory_db

        config_key = 'Fake key'
        config_value = 'Fake value'

        new_config = Configurations(config_key=config_key, config_value=config_value)

        session.add(new_config)
        session.commit()

        inserted_config = session.query(Configurations).filter_by(config_key=config_key).first()

        assert inserted_config is not None, "Конфигурация должна быть вставлена"
        assert inserted_config.config_key == config_key, f"Ключ должен быть {config_key}"
        assert inserted_config.config_value == config_value, f"Значение должно быть {config_value}"
