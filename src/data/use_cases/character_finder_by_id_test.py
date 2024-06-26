from src.infra.db.tests.character_repository import CharacterRepositorySpy
from .character_finder_by_id import CharacterFinderById

def test_find_character_by_id():
    name = 'Ola'
    sin = 'Mundo'
    description = '!'
    sacred_treasure = None

    repo = CharacterRepositorySpy()

    repo.insert_character(name, sin, description, sacred_treasure)

    character_id = repo.characters[0].id

    character = CharacterFinderById(repo)
    response = character.find_character_by_id(character_id)

    assert response["type"] == "Characters"
    assert response["count"] == 1
    assert response["attributtes"]["id"] == character_id
    assert response["attributtes"]["name"] == name
    assert response["attributtes"]["sin"] == sin
    assert response["attributtes"]["description"] == description
    assert response["attributtes"]["sacred_treasure"] == sacred_treasure
