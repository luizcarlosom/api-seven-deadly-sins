from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

async def character_create_validator(request: any):
    body_validator = Validator({
        "name": {"type": "string", "required": True, "empty": False},
        "sin": {"type": "string", "required": True, "empty": False},
        "description": {"type": "string", "required": True, "empty": False},
        "sacred_treasure": {"type": "string", "required": True, "empty": False, "nullable": True},
    })

    request_body = await request.json()
    response = body_validator.validate(request_body)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
