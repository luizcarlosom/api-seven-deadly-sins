#pylint: disable=redefined-builtin, too-many-arguments, broad-exception-raised

from typing import Dict, Optional

class CharacterUpdateSpy:
    
    def __init__(self) -> None:
        self.character = ''

    def update(
        self,
        id: int, 
        name: Optional[str] = None,
        sin: Optional[str] = None,
        description: Optional[str] = None,
        sacred_treasure: Optional[str] = None
    ) -> Dict:
        
        characters = [
            { 
                "id": 1, 
                "name": "Hellow", 
                "sin": "World", 
                "description": "!", 
                "sacred_treasure": "!" 
            }
        ]

        self.character = next((c for c in characters if c["id"] == id), None)

        if self.character is None: raise Exception('Invalid ID')

        if name is not None:
            self.character["name"] = name
        if sin is not None:
            self.character["sin"] = sin
        if description is not None:
            self.character["description"] = description
        if sacred_treasure is not None:
            self.character["sacred_treasure"] = sacred_treasure

        response = {
            "type": "Characters",
            "count": 1,
            "attributtes": { 
                    "id": self.character["id"], 
                    "name": self.character["name"], 
                    "sin": self.character["sin"], 
                    "description": self.character["description"], 
                    "sacred_treasure": self.character["sacred_treasure"] 
            }
        }

        return response
