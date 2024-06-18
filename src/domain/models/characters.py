#pylint: disable=redefined-builtin, too-many-arguments

class Characters:
    def __init__(
        self, 
        id: int, 
        name: str, 
        sin: str, 
        description: str,
        image_base64: str,
        sacred_treasure: str
    ) -> None:
        self.id = id
        self.name = name
        self.sin = sin
        self.description = description
        self.image_base64: image_base64
        self.sacred_treasure: sacred_treasure
