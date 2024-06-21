# pylint: disable=broad-exception-raised
from typing import Optional, Dict
from src.domain.use_cases.character_create import CharacterCreate as CharacterCreateInterface
from src.data.interfaces.character_repository import CharacterRepositoryInterface

class CharacterCreate(CharacterCreateInterface):
    def __init__(self, character_repository: CharacterRepositoryInterface) -> None:
        self.__character_repository = character_repository

    def create(
        self, 
        name: str,
        sin: str,
        description: str,
        sacred_treasure: Optional[str] = None
    ) -> Dict: 
        self.__validate_field('name', name)
        self.__validate_field('sin', sin)
        self.__validate_field('description', description)
        self.__validate_field('sacred_treasure', sacred_treasure)
        
        self.__registry_character_information(name, sin, description, sacred_treasure)
        response = self.__format_response(name, sin, description, sacred_treasure)
        return response

    @classmethod
    def __validate_field(cls, name_field: str, content_field: Optional[str]) -> None:
        if name_field != 'sacred_treasure' and not content_field:
            raise Exception(f'The {name_field} field cannot be empty')

        if content_field is not None and not isinstance(content_field, str):
            raise Exception(f'The {name_field} field is invalid for character creation')    

        if content_field is not None and len(content_field) > 36:
            if name_field != 'description':
                raise Exception(f'The {name_field} field has more characters than it should')

    def __registry_character_information(
        self,
        name: str,
        sin: str,
        description: str,
        sacred_treasure: Optional[str] = None
    ) -> None:
        self.__character_repository.insert_character(name, sin, description, sacred_treasure)

    @classmethod
    def __format_response(
            cls,
            name: str,
            sin: str,
            description: str,
            sacred_treasure: Optional[str] = None
        ) -> Dict: 
        response = {
            "type": "Characters",
            "count": 1,
            "attributtes": {
                "name": name,
                "sin": sin,
                "description": description,
                "sacred_treasure": sacred_treasure
            }
        }
        return response
