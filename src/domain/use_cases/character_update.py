# pylint: disable=too-many-arguments, redefined-builtin
from abc import ABC, abstractmethod
from typing import Dict, Optional

class CharacterUpdate(ABC):

    @abstractmethod
    def update(
        self, 
        id: str, 
        name: Optional[str] = None, 
        sin: Optional[str] = None, 
        description: Optional[str] = None, 
        image_base64: Optional[str] = None, 
        sacred_treasure: Optional[str] = None
    ) -> Dict: pass
