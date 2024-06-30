from src.presentation.controllers.character_update_controller import (
    CharacterUpdateController
)
from src.data.tests.character_update import CharacterUpdateSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.body = {
            "id": 1,
            "name": "Ola",
            "sin": "Mundo"
        }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = CharacterUpdateSpy()
    character_create_controller = CharacterUpdateController(use_case)

    response = character_create_controller.handle(http_request_mock)
    
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200

    assert response.body["data"]["type"] == "Characters"
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["attributtes"]["id"] == http_request_mock.body["id"]
    assert response.body["data"]["attributtes"]["name"] == http_request_mock.body["name"]
    assert response.body["data"]["attributtes"]["sin"] == http_request_mock.body["sin"]
    