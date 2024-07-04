from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

async def character_update_validator(request: any):
    body_validator = Validator({
        "id": {"type": "integer", "required": True, "empty": False, "nullable": False},
        "name": {"type": "string", "required": False, "empty": False, "nullable": False},
        "sin": {"type": "string", "required": False, "empty": False, "nullable": False},
        "description": {"type": "string", "required": False, "empty": False, "nullable": False},
        "sacred_treasure": {"type": "string", "required": False, "empty": False, "nullable": True},
    })

    request_body = await request.json()
    response = body_validator.validate(request_body)
    
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
