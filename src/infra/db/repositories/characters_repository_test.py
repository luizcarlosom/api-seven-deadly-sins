import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .characters_repository import CharacterRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive teste")
def test_insert_character():
    mocked_name = 'Meliodas'
    mocked_sin = 'Ira'
    mocked_description = 'Lider dos 7 pecados capitais'
    mocked_image_base64 = '@asdsnj345ugfman'
    mocked_sacred_treasure = 'Espada Sagrada'

    characters_repository = CharacterRepository()
    characters_repository.insert_character(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_image_base64,
        mocked_sacred_treasure
    )

    sql = '''
        SELECT * FROM characters
        WHERE name = '{}'
        AND sin = '{}'
        AND description = '{}'
        AND image_base64 = '{}'
        AND sacred_treasure = '{}'
    '''.format(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_image_base64,
        mocked_sacred_treasure
    )
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.sin == mocked_sin
    assert registry.description == mocked_description
    assert registry.image_base64 == mocked_image_base64
    assert registry.sacred_treasure == mocked_sacred_treasure

    connection.execute(text(f'''
        DELETE FROM characters WHERE id = {registry.id}
    '''))
    connection.commit()
