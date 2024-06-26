# pylint: disable=broad-exception-raised, redefined-builtin
from typing import Dict
from src.domain.use_cases.character_finder_by_id import (
    CharacterFinderById  as CharacterFinderByIdInterface
)
from src.data.interfaces.character_repository import CharacterRepositoryInterface
from src.domain.models.characters import Characters

class CharacterFinderById(CharacterFinderByIdInterface):
    def __init__(self, character_repository: CharacterRepositoryInterface) -> None:
        self.__character_repository = character_repository

    def find_character_by_id(self, id: int) -> Dict: 
        character = self.__search_character(id)
        response = self.__format_response(character)
        return response

    def __search_character(self, id: int) -> Characters:
        character = self.__character_repository.select_character(id)
        if character is None: raise Exception('Invalid ID')
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
