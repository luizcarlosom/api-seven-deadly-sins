from src.infra.db.repositories.characters_repository import CharacterRepository
from src.data.use_cases.character_delete import CharacterDelete
from src.presentation.controllers.character_delete_controller import CharacterDeleteController

def character_delete_composer():
    repository = CharacterRepository()
    use_case = CharacterDelete(repository)
    controller = CharacterDeleteController(use_case)

    return controller.handle
