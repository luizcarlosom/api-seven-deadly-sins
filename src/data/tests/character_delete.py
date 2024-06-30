#pylint: disable=redefined-builtin

from typing import Dict

class CharacterDeleteSpy:
    
    def __init__(self) -> None:
        self.message = ''
        self.character = ''

    def delete(self, id: int) -> Dict:
        characters = [
            { 
                "id": 1, 
                "name": "name", 
                "sin": "sin", 
                "description": "description", 
                "sacred_treasure": "sacred_treasure" 
            }
        ]

        self.character = next((c for c in characters if c["id"] == id), None)

        if self.character:
            characters.remove(self.character)
            self.message = f"The {self.character['name']} character has been deleted"
        else:
            self.message = f"Character with id {id} does not exist."

            
        return  {
            "type": "String",
            "count": 1,
            "attributtes": {
                "message": self.message
            }
        }
