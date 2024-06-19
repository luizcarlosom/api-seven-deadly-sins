# pylint: disable=redefined-builtin
from abc import ABC, abstractmethod

class CharacterDelete(ABC):

    @abstractmethod
    def delete(self, id: int) -> None: pass
