# pylint: disable=too-many-arguments, redefined-builtin
from typing import List, Optional
from src.data.interfaces.character_repository import CharacterRepositoryInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.characters import Characters as CharactersEntity
from src.domain.models.characters import Characters

class CharacterRepository(CharacterRepositoryInterface):

    @classmethod
    def insert_character(
            cls, 
            name: str, 
            sin: str, 
            description: str, 
            sacred_treasure: Optional[str] = None
        ) -> None:
    
        with DBConnectionHandler() as database:
            try: 
                new_registry = CharactersEntity(
                    name=name,
                    sin=sin,
                    description=description,
                    sacred_treasure=sacred_treasure
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    @classmethod
    def delete_character(cls, id: str) -> None: 
        with DBConnectionHandler() as database:
            try:
                character = (
                    database.session
                        .query(CharactersEntity)
                        .filter(CharactersEntity.id == id)
                        .delete()
                )
                database.session.commit()
                return character
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    @classmethod
    def select_character(cls, id: str) -> Characters: 
        with DBConnectionHandler() as database:
            try:
                character = (
                    database.session
                        .query(CharactersEntity)
                        .filter(CharactersEntity.id == id)
                        .one_or_none()
                )
                return character
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    @classmethod
    def select_all_characters(cls) -> List[Characters]: 
        with DBConnectionHandler() as database:
            try:
                character = (
                    database.session
                        .query(CharactersEntity)
                        .all()
                )
                return character
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update_character(
            cls, 
            id: str, 
            name: Optional[str] = None, 
            sin: Optional[str] = None, 
            description: Optional[str] = None, 
            sacred_treasure: Optional[str] = None
        ) -> Characters: 

        with DBConnectionHandler() as database:
            try:
                character = (
                    database.session
                        .query(CharactersEntity)
                        .filter(CharactersEntity.id == id)
                        .one_or_none()
                )
                
                if character:
                    if name is not None:
                        character.name = name
                    if sin is not None:
                        character.sin = sin
                    if description is not None:
                        character.description = description
                    if sacred_treasure is not None:
                        character.sacred_treasure = sacred_treasure

                    database.session.commit()
                return character
            except Exception as exception:
                database.session.rollback()
                raise exception
