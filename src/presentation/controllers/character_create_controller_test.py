from src.presentation.controllers.character_create_controller import (
    CharacterCreateController
)
from src.data.tests.character_create import CharacterCreateSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "name": "Hello",
            "sin": "world",
            "description": "!",
            "sacred_treasure": "!"
        }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = CharacterCreateSpy()
    character_create_controller = CharacterCreateController(use_case)

    response = character_create_controller.handle(http_request_mock)
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 201

    assert response.body["data"]["type"] == "Characters"
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["attributtes"] is not None
    