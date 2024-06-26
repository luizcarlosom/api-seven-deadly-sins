#pylint: disable=redefined-builtin
from typing import Optional, List
from src.domain.models.characters import Characters

class CharacterRepositorySpy:
    def __init__(self) -> None:
        self.create_character_attributtes = {}
        self.delete_character_attributtes = {}
        self.characters = []

    def insert_character(
        self,
        name: str,
        sin: str,
        description: str,
        sacred_treasure: Optional[str] = None
    ) -> None:
        id = len(self.characters) + 1
        character = Characters(
            id=id, 
            name=name, 
            sin=sin, 
            description=description, 
            sacred_treasure=sacred_treasure)

        self.characters.append(character)

        self.create_character_attributtes['name'] = name
        self.create_character_attributtes['sin'] = sin
        self.create_character_attributtes['description'] = description
        self.create_character_attributtes['sacred_treasure'] = sacred_treasure

    def delete_character(self, id: int) -> Optional[Characters]:
        character = next((c for c in self.characters if c.id == id), None)
        if character:
            self.characters.remove(character)
        self.delete_character_attributtes['id'] = id
        return character

    def select_all_characters(self) -> List[Characters]:
        return self.characters

    def select_character(self, id: int) -> Optional[Characters]:
        return next((c for c in self.characters if c.id == id), None )
