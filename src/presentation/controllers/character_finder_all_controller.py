from typing import Optional
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.character_finder_all import (
    CharacterFinderAll as CharacterFinderAllInterface
)

class CharacterFinderAllController(ControllerInterface):

    def __init__(self, use_case: CharacterFinderAllInterface) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: Optional[HttpRequest]=None) -> HttpResponse:
        response = self.__use_case.find_all_characters()

        return HttpResponse(
            status_code=200,
            body={ "data": response}
        )
