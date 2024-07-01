from src.infra.db.repositories.characters_repository import CharacterRepository
from src.data.use_cases.character_finder_by_id import CharacterFinderById
from src.presentation.controllers.character_finder_by_id_controller import (
    CharacterFinderByIdController
)

def character_finder_by_id_composer():
    repository = CharacterRepository()
    use_case = CharacterFinderById(repository)
    controller = CharacterFinderByIdController(use_case)

    return controller.handle
