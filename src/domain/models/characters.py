#pylint: disable=redefined-builtin, too-many-arguments
from typing import Optional

class Characters:
    def __init__(
        self, 
        id: int, 
        name: str, 
        sin: str, 
        description: str,
        sacred_treasure: Optional[str] = None
    ) -> None:
        self.id = id
        self.name = name
        self.sin = sin
        self.description = description
        self.sacred_treasure = sacred_treasure
