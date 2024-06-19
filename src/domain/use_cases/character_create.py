# pylint: disable=too-many-arguments
from abc import ABC, abstractmethod
from typing import Dict, Optional

class CharacterCreate(ABC):

    @abstractmethod
    def create(
        self, 
        name: str,
        sin: str,
        description: str,
        image_base64: bytes,
        sacred_treasure: Optional[str] = None
    ) -> Dict: pass
