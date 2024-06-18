# pylint: disable=too-many-arguments
from src.data.interfaces.character_repository import CharacterRepositoryInterface
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.characters import Characters as CharactersEntity

class CharacterRepository(CharacterRepositoryInterface):

    @classmethod
    def insert_character(
            cls, 
            name: str, 
            sin: str, 
            description: str, 
            image_base64: str, 
            sacred_treasure: str | None
        ) -> None:
    
        with DBConnectionHandler() as database:
            try: 
                new_registry = CharactersEntity(
                    name=name,
                    sin=sin,
                    description=description,
                    image_base64=image_base64,
                    sacred_treasure=sacred_treasure
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    @classmethod
    def delete_character(cls, name: str) -> None: pass

    @classmethod
    def select_character(cls, name: str) -> None: pass

    @classmethod
    def select_all_characters(cls) -> None: pass
