#pylint: disable=redefined-builtin

from typing import Dict, Optional

class CharacterCreateSpy:

    def create(
        self, 
        name: str,
        sin: str,
        description: str,
        sacred_treasure: Optional[str] = None
    ) -> Dict:
        
        attributes = { 
            "id": 1, 
            "name": name, 
            "sin": sin, 
            "description": description, 
            "sacred_treasure": sacred_treasure 
        }

        return  {
            "type": "Characters",
            "count": 1,
            "attributtes": attributes
        }
