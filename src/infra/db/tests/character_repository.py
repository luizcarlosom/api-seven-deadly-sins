#pylint: disable=redefined-builtin
from typing import Optional, Dict, List

class CharacterRepositorySpy:
    def __init__(self) -> None:
        self.create_character_attributtes = {}
        self.delete_character_attributtes = {}
        self.characters = {} 

    def insert_character(
        self,
        name: str,
        sin: str,
        description: str,
        sacred_treasure: Optional[str] = None
    ) -> None:
        id = len(self.characters) + 1
        self.characters[id] = {
            'name': name,
            'sin': sin,
            'description': description,
            'sacred_treasure': sacred_treasure
        }
        self.create_character_attributtes['name'] = name
        self.create_character_attributtes['sin'] = sin
        self.create_character_attributtes['description'] = description
        self.create_character_attributtes['sacred_treasure'] = sacred_treasure

    def delete_character(self, id: int) -> Dict:
        character = self.characters.pop(id, None)
        self.delete_character_attributtes['id'] = id
        return character

    def select_character(self, id: int) -> List[Dict]:
        character = self.characters.get(id)
        if character:
            return [character]
        return []
