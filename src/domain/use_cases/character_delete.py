# pylint: disable=redefined-builtin
from typing import Dict
from abc import ABC, abstractmethod

class CharacterDelete(ABC):

    @abstractmethod
    def delete(self, id: int) -> Dict: pass
