#pylint: disable=redefined-builtin

from typing import Dict

class CharacterFinderByIdSpy:

    def __init__(self) -> None:
        self.find_character_by_id_attributes = {}

    def find_character_by_id(self, id: int) -> Dict:
        self.find_character_by_id_attributes["id"] = id

        return  {
            "type": "Characters",
            "count": 1,
            "attributtes": { 
                    "id": self.find_character_by_id_attributes["id"], 
                    "name": "name", 
                    "sin": "sin", 
                    "description": "description", 
                    "sacred_treasure": "sacred_treasure" 
            }
        }
