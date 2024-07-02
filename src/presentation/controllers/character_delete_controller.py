#pylint: disable=redefined-builtin

from typing import Optional
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.character_delete import CharacterDelete as CharacterDeleteInterface

class CharacterDeleteController(ControllerInterface):

    def __init__(self, use_case: CharacterDeleteInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: Optional[HttpRequest]=None) -> HttpResponse:
        id = http_request.path_params["id"]
        
        response = self.__use_case.delete(id)
    
        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )
    