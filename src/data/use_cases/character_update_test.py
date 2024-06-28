from src.infra.db.tests.character_repository import CharacterRepositorySpy
from .character_update import CharacterUpdate

def test_character_update():
    name = 'Ola'
    sin = 'Mundo'
    description = '!'
    sacred_treasure = None

    repo = CharacterRepositorySpy()

    repo.insert_character(name, sin, description, sacred_treasure)

    character = CharacterUpdate(repo)
    
    character_id = 1
    updated_name = 'Hello'
    update_sin = 'World'

    result = character.update(character_id, updated_name, update_sin)
    
    assert result["type"] == "Characters"
    assert result["count"] == 1

    assert result["attributtes"]["id"] == character_id
    assert result["attributtes"]["name"] == updated_name
    assert result["attributtes"]["sin"] == update_sin
    assert result["attributtes"]["description"] == description
    assert result["attributtes"]["sacred_treasure"] == sacred_treasure
