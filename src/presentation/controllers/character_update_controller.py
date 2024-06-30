#pylint: disable=redefined-builtin

from typing import Optional
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.character_update import CharacterUpdate as CharacterUpdateInterface

class CharacterUpdateController(ControllerInterface):

    def __init__(self, use_case: CharacterUpdateInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Optional[HttpRequest]=None) -> HttpResponse:
        id = http_request.body.get("id")
        name = http_request.body.get("name")
        sin = http_request.body.get("sin")
        description = http_request.body.get("description")
        sacred_treasure = http_request.body.get("sacred_treasure")
        
        response = self.__use_case.update(id, name, sin, description, sacred_treasure)
    
        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )
    