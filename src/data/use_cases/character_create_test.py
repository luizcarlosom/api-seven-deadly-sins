from src.infra.db.tests.character_repository import CharacterRepositorySpy
from .character_create import CharacterCreate

def test_create():
    name = 'Ola'
    sin = 'Mundo'
    description = '!'
    sacred_treasure = None

    repo = CharacterRepositorySpy()
    character_create = CharacterCreate(repo)

    response = character_create.create(name, sin, description, sacred_treasure)

    assert repo.create_character_attributtes["name"] == name
    assert repo.create_character_attributtes["sin"] == sin
    assert repo.create_character_attributtes["description"] == description
    assert repo.create_character_attributtes["sacred_treasure"] == sacred_treasure

    assert response["type"] == "Characters"
    assert response["count"] == 1
    assert response["attributtes"]
