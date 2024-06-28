from src.data.tests.character_finder_all import CharacterFinderAllSpy
from src.presentation.controllers.character_finder_all_controller import (
    CharacterFinderAllController
)

def test_handle():
    use_case = CharacterFinderAllSpy()
    character_finder_all_controller = CharacterFinderAllController(use_case)

    response = character_finder_all_controller.handle()

    assert response.status_code == 200
    assert response.body["data"]["type"] == "Characters"
    assert response.body["data"]["attributtes"]
    assert response.body["data"]["count"] == len(response.body["data"]["attributtes"])
