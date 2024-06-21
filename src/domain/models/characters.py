#pylint: disable=redefined-builtin, too-many-arguments

class Characters:
    def __init__(
        self, 
        id: int, 
        name: str, 
        sin: str, 
        description: str,
        sacred_treasure: str
    ) -> None:
        self.id = id
        self.name = name
        self.sin = sin
        self.description = description
        self.sacred_treasure: sacred_treasure
