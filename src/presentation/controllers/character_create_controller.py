from typing import Optional
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.character_create import CharacterCreate as CharacterCreateInterface

class CharacterCreateController(ControllerInterface):

    def __init__(self, use_case: CharacterCreateInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Optional[HttpRequest]=None) -> HttpResponse:
        name = http_request.body["name"]
        sin = http_request.body["sin"]
        description = http_request.body["description"]
        sacred_treasure = http_request.body["sacred_treasure"]
        
        response = self.__use_case.create(name, sin, description, sacred_treasure)
    
        return HttpResponse(
            status_code=201,
            body={ "data": response }
        )
    