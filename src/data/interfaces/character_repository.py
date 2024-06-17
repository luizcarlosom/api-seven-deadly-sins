#pylint: disable=too-many-arguments

from typing import List
from abc import ABC, abstractmethod
from src.domain.models.characters import Characters

class CharacterRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_character(
        self, 
        name: str, 
        sin: str, 
        description: str, 
        image_base64: str, 
        sacred_treasue: str | None
    ) -> None: pass

    @abstractmethod
    def delete_character(self, name: str) -> None: pass

    @abstractmethod
    def select_character(self, name: str) -> Characters: pass

    @abstractmethod
    def select_all_characters(self) -> List[Characters]: pass
