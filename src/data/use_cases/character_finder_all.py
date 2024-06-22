# pylint: disable=broad-exception-raised, redefined-builtin
from typing import List, Dict
from src.domain.use_cases.character_finder_all import (
    CharacterFinderAll as CharacterFinderAllInterface
)
from src.data.interfaces.character_repository import CharacterRepositoryInterface
from src.domain.models.characters import Characters

class CharacterFinderAll(CharacterFinderAllInterface):
    def __init__(self, character_repository: CharacterRepositoryInterface) -> None:
        self.__character_repository = character_repository

    def find_all_characters(self) -> List[Dict]: 
        characters = self.__search_all_characters()
        response = self.__format_response(characters)
        return response

    def __search_all_characters(self) -> List[Characters]:
        characters = self.__character_repository.select_all_characters()
        return characters

    @classmethod
    def __format_response(cls, characters: List[Characters]) -> List[Dict]:
        attributtes = []
        for character in characters:
            attributtes.append(
                { 
                    "id": character.id, 
                    "name": character.name, 
                    "sin": character.sin, 
                    "description": character.description, 
                    "sacred_treasure": character.sacred_treasure 
                }
            )
        
        response = {
            "type": "Characters",
            "count": len(characters),
            "attributtes": attributtes
        }

        return response
