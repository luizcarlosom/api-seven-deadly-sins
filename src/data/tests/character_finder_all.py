#pylint: disable=redefined-builtin

from typing import Dict, List

class CharacterFinderAllSpy:
    
    def find_all_characters(self) -> List[Dict]:
        attributes =  [
                { 
                    "id": 1, 
                    "name": "name", 
                    "sin": "sin", 
                    "description": "description", 
                    "sacred_treasure": "sacred_treasure" 
                },
                { 
                    "id": 2, 
                    "name": "name2", 
                    "sin": "sin2", 
                    "description": "description2", 
                    "sacred_treasure": "sacred_treasure2" 
            }
        ]

        return  {
            "type": "Characters",
            "count": len(attributes),
            "attributtes": attributes
        }
