from abc import ABC, abstractmethod
from typing import List, Dict

class CharacterFinderAll(ABC):

    @abstractmethod
    def find_all_characters(self) -> List[Dict]: pass
