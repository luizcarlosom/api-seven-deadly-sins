from src.presentation.controllers.character_finder_by_id_controller import (
    CharacterFinderByIdController
)
from src.data.tests.character_finder_by_id import CharacterFinderByIdSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = { "id": "1" }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = CharacterFinderByIdSpy()
    character_finder_by_id_controller = CharacterFinderByIdController(use_case)

    response = character_finder_by_id_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
