#pylint: disable=too-many-arguments, redefined-builtin

from typing import List, Optional
from abc import ABC, abstractmethod
from src.domain.models.characters import Characters

class CharacterRepositoryInterface(ABC):
    
    @abstractmethod
    def insert_character(
        self, 
        name: str, 
        sin: str, 
        description: str, 
        image_base64: bytes, 
        sacred_treasue: Optional[str] = None
    ) -> None: pass

    @abstractmethod
    def delete_character(self, id: str) -> None: pass

    @abstractmethod
    def select_character(self, id: str) -> Characters: pass

    @abstractmethod
    def select_all_characters(self) -> List[Characters]: pass

    @abstractmethod
    def update_character(
        self, 
        id: str, 
        name: Optional[str] = None, 
        sin: Optional[str] = None, 
        description: Optional[str] = None, 
        image_base64: Optional[bytes] = None, 
        sacred_treasue: Optional[str] = None
    ) -> None: pass
