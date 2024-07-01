from src.infra.db.repositories.characters_repository import CharacterRepository
from src.data.use_cases.character_update import CharacterUpdate
from src.presentation.controllers.character_update_controller import (
    CharacterUpdateController
)

def character_update_composer():
    repository = CharacterRepository()
    use_case = CharacterUpdate(repository)
    controller = CharacterUpdateController(use_case)

    return controller.handle
