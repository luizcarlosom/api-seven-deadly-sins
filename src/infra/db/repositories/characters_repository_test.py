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
    mocked_sacred_treasure = 'Espada Sagrada'

    characters_repository = CharacterRepository()
    characters_repository.insert_character(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )

    sql = '''
        SELECT * FROM characters
        WHERE name = '{}'
        AND sin = '{}'
        AND description = '{}'
        AND sacred_treasure = '{}'
    '''.format(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.sin == mocked_sin
    assert registry.description == mocked_description
    assert registry.sacred_treasure == mocked_sacred_treasure

    connection.execute(text(f'''
        DELETE FROM characters WHERE id = {registry.id}
    '''))
    connection.commit()

@pytest.mark.skip(reason="Sensive teste")
def test_delete_character():
    mocked_name = 'Meliodas'
    mocked_sin = 'Ira'
    mocked_description = 'Lider dos 7 pecados capitais'
    mocked_sacred_treasure = 'Espada Sagrada'

    characters_repository = CharacterRepository()
    characters_repository.insert_character(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )

    sql_select = '''
        SELECT * FROM characters
        WHERE name = '{}'
        AND sin = '{}'
        AND description = '{}'
        AND sacred_treasure = '{}'
    '''.format(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )

    reponse = connection.execute(text(sql_select))
    registry = reponse.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.sin == mocked_sin
    assert registry.description == mocked_description
    assert registry.sacred_treasure == mocked_sacred_treasure

    characters_repository.delete_character(registry.id)

    connection.close()
    connection_after = db_connection_handler.get_engine().connect()

    response_after_delete = connection_after.execute(text(sql_select))
    deleted_registry = response_after_delete.fetchall()
    
    assert len(deleted_registry) == 0

@pytest.mark.skip(reason="Sensive teste")
def test_select_character():
    mocked_name = 'Meliodas'
    mocked_sin = 'Ira'
    mocked_description = 'Lider dos 7 pecados capitais'
    mocked_sacred_treasure = 'Espada Sagrada'

    characters_repository = CharacterRepository()
    characters_repository.insert_character(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )

    sql_select = '''
        SELECT * FROM characters
        WHERE name = '{}'
        AND sin = '{}'
        AND description = '{}'
        AND sacred_treasure = '{}'
    '''.format(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )

    response = connection.execute(text(sql_select))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.sin == mocked_sin
    assert registry.description == mocked_description
    assert registry.sacred_treasure == mocked_sacred_treasure

    selected_character = characters_repository.select_character(registry.id)
    
    assert selected_character.id == registry.id
    assert selected_character.name == mocked_name
    assert selected_character.sin == mocked_sin
    assert selected_character.description == mocked_description
    assert selected_character.sacred_treasure == mocked_sacred_treasure

    characters_repository.delete_character(registry.id)
    connection.close()

@pytest.mark.skip(reason="Sensive teste")
def test_select_all_characters():
    mocked_characters = [
        {
            'name': 'Meliodas',
            'sin': 'Ira',
            'description': 'Lider dos 7 pecados capitais',
            'sacred_treasure': 'Espada Sagrada'
        },
        {
            'name': 'Ban',
            'sin': 'Ganância',
            'description': 'Imortal',
            'sacred_treasure': 'Couro de Raposa'
        }
    ]

    characters_repository = CharacterRepository()

    for character in mocked_characters:
        characters_repository.insert_character(
            character['name'],
            character['sin'],
            character['description'],
            character['sacred_treasure']
        )

    all_characters = characters_repository.select_all_characters()

    assert len(all_characters) == len(mocked_characters)

    for character in mocked_characters:
        found = False
        for db_character in all_characters:
            if (db_character.name == character['name'] and
                db_character.sin == character['sin'] and
                db_character.description == character['description'] and
                db_character.sacred_treasure == character['sacred_treasure']):
                found = True
                break
        assert found

    for character in all_characters:
        characters_repository.delete_character(character.id)
    connection.close()

@pytest.mark.skip(reason="Sensive teste")
def test_update_character():
    mocked_name = 'Meliodas'
    mocked_sin = 'Ira'
    mocked_description = 'Lider dos 7 pecados capitais'
    mocked_sacred_treasure = 'Espada Sagrada'

    characters_repository = CharacterRepository()
    characters_repository.insert_character(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )

    sql_select = '''
        SELECT * FROM characters
        WHERE name = '{}'
        AND sin = '{}'
        AND description = '{}'
        AND sacred_treasure = '{}'
    '''.format(
        mocked_name,
        mocked_sin,
        mocked_description,
        mocked_sacred_treasure
    )

    response = connection.execute(text(sql_select))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.sin == mocked_sin
    assert registry.description == mocked_description
    assert registry.sacred_treasure == mocked_sacred_treasure


    updated_name = 'Meliodas Updated'
    updated_sin = 'Ira Updated'
    updated_description = 'Lider dos 7 pecados capitais Updated'
    updated_sacred_treasure = 'Nova Espada Sagrada'

    characters_repository.update_character(
        registry.id,
        name=updated_name,
        sin=updated_sin,
        description=updated_description,
        sacred_treasure=updated_sacred_treasure
    )
    
    updated_registry = characters_repository.select_character(registry.id)

    assert updated_registry.name == updated_name
    assert updated_registry.sin == updated_sin
    assert updated_registry.description == updated_description
    assert updated_registry.sacred_treasure == updated_sacred_treasure

    connection.execute(text(f'''
        DELETE FROM characters WHERE id = {registry.id}
    '''))
    connection.commit()
