from src.infra.db.tests.character_repository import CharacterRepositorySpy
from .character_finder_all import CharacterFinderAll

def test_find_all_characters():
    name = 'Ola'
    sin = 'Mundo'
    description = '!'
    sacred_treasure = None

    repo = CharacterRepositorySpy()

    repo.insert_character(name, sin, description, sacred_treasure)
    repo.insert_character(name, sin, description, sacred_treasure)

    characters = CharacterFinderAll(repo)
    result = characters.find_all_characters()

    assert result["type"] == "Characters"
    assert result["count"] == 2

    assert result["attributtes"][0]['name'] == name
    assert result["attributtes"][0]['sin'] == sin
    assert result["attributtes"][0]['description'] == description
    assert result["attributtes"][0]['sacred_treasure'] == sacred_treasure

    assert result["attributtes"][1]['name'] == name
    assert result["attributtes"][1]['sin'] == sin
    assert result["attributtes"][1]['description'] == description
    assert result["attributtes"][1]['sacred_treasure'] == sacred_treasure
