from src.infra.db.repositories.characters_repository import CharacterRepository
from src.data.use_cases.character_finder_all import CharacterFinderAll
from src.presentation.controllers.character_finder_all_controller import (
    CharacterFinderAllController
)

def character_finder_all_composer():
    repository = CharacterRepository()
    use_case = CharacterFinderAll(repository)
    controller = CharacterFinderAllController(use_case)

    return controller.handle
