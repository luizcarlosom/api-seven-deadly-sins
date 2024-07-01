from src.infra.db.repositories.characters_repository import CharacterRepository
from src.data.use_cases.character_create import CharacterCreate
from src.presentation.controllers.character_create_controller import CharacterCreateController

def character_create_composer():
    repository = CharacterRepository()
    use_case = CharacterCreate(repository)
    controller = CharacterCreateController(use_case)

    return controller.handle
