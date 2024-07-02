from src.presentation.controllers.character_delete_controller import (
    CharacterDeleteController
)
from src.data.tests.character_delete import CharacterDeleteSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.path_params = { "id": 1 }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = CharacterDeleteSpy()
    character_delete_controller = CharacterDeleteController(use_case)

    response = character_delete_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 204

    assert response.body["data"]["type"] == "String"
    assert response.body["data"]["count"] == 1
    assert response.body["data"]["attributtes"]["message"] == "The name character has been deleted"
