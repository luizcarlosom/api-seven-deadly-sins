# pylint: disable=broad-exception-raised, redefined-builtin
from typing import Dict
from src.domain.use_cases.character_delete import CharacterDelete as CharacterDeleteInterface
from src.data.interfaces.character_repository import CharacterRepositoryInterface

class CharacterDelete(CharacterDeleteInterface):
    def __init__(self, character_repository: CharacterRepositoryInterface) -> None:
        self.__character_repository = character_repository

    def delete(self, id: int) -> Dict: 
        character = self.__validate_id(id)
        self.__delete_character(id)
        response = self.__format_response(f"The {character.name} character has been deleted")
        return response
       

    def __delete_character(self, id: int) -> None:
        success = self.__character_repository.delete_character(id)
        if not success:
            raise Exception(f"Character with id {id} does not exist.")

    def __validate_id(self, id: int) -> Dict:
        character = self.__character_repository.select_character(id)
        if character is None: raise Exception('Invalid ID')
        return character

    @classmethod
    def __format_response(cls, message: str) -> Dict: 
        response = {
            "type": "String",
            "count": 1,
            "attributtes": {
                "message": message
            }
        }
        return response
