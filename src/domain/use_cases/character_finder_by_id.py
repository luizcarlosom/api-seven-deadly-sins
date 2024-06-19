# pylint: disable=redefined-builtin
from abc import ABC, abstractmethod
from typing import Dict

class CharacterFinderById(ABC):

    @abstractmethod
    def find_character_by_id(self, id: int) -> Dict: pass
