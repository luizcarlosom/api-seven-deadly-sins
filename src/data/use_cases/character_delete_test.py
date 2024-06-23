from src.infra.db.tests.character_repository import CharacterRepositorySpy
from .character_delete import CharacterDelete

def test_delete():
    name = 'Ola'
    sin = 'Mundo'
    description = '!'
    sacred_treasure = None

    repo = CharacterRepositorySpy()
    character_delete = CharacterDelete(repo)

    repo.insert_character(name, sin, description, sacred_treasure)

    character_id = 1
    assert repo.characters[character_id]['name'] == name

    response = character_delete.delete(character_id)

    assert repo.delete_character_attributtes["id"] == character_id
    assert response["type"] == "String"
    assert response["count"] == 1
    assert response["attributtes"]["message"] == f"The {name} character has been deleted"
    assert character_id not in repo.characters
