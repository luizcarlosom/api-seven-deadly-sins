# pylint: disable=broad-exception-raised, redefined-builtin, too-many-arguments
from typing import Dict, Optional
from src.domain.use_cases.character_update import CharacterUpdate  as CharacterUpdateInterface
from src.data.interfaces.character_repository import CharacterRepositoryInterface
from src.domain.models.characters import Characters

class CharacterFinderById(CharacterUpdateInterface):
    def __init__(self, character_repository: CharacterRepositoryInterface) -> None:
        self.__character_repository = character_repository

    def update(
        self, 
        id: str, 
        name: Optional[str] = None, 
        sin: Optional[str] = None, 
        description: Optional[str] = None, 
        sacred_treasure: Optional[str] = None
    ) -> Dict: 
        self.__validate_id(id)
        character = self.__update_character(
            id,
            name,
            sin,
            description,
            sacred_treasure
        ) 
        response = self.__format_response(character)
        return response

    def __validate_id(self, id: int):
        character = self.__character_repository.select_character(id)
        if len(character) == 0: raise Exception('Invalid ID')
        
    def __update_character(
            self, 
            id: int,
            name: Optional[str] = None, 
            sin: Optional[str] = None, 
            description: Optional[str] = None, 
            sacred_treasure: Optional[str] = None    
    ) -> Characters:
        character = self.__character_repository.update_character(
            id, 
            name, 
            sin, 
            description, 
            sacred_treasure
        )
        return character

    @classmethod
    def __format_response(cls, character: Characters) -> Dict:
        response = {
            "type": "Characters",
            "count": 1,
            "attributtes": { 
                    "id": character.id, 
                    "name": character.name, 
                    "sin": character.sin, 
                    "description": character.description, 
                    "sacred_treasure": character.sacred_treasure 
            }
        }
        return response
