from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

# Import Adapters
from src.main.adapters.request_adapter import request_adapter

# Import Character Composers 
from src.main.composers.character_finder_all_composer import character_finder_all_composer
from src.main.composers.character_create_composer import character_create_composer
from src.main.composers.character_finder_by_id_composer import character_finder_by_id_composer
from src.main.composers.character_delete_composer import character_delete_composer
from src.main.composers.character_upate_composer import character_update_composer

character_router = APIRouter(prefix="/api/character", tags=["Character"])

@character_router.post("/")
async def create_character(request: Request): 
    http_response = await request_adapter(request, character_create_composer())
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@character_router.get("/")
async def list_characters(request: Request):
    http_response = await request_adapter(request, character_finder_all_composer())
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@character_router.get("/{id}")
async def get_character(request: Request): 
    http_response = await request_adapter(request, character_finder_by_id_composer())
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@character_router.put("/")
async def update_character(request: Request): 
    http_response = await request_adapter(request, character_update_composer())
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@character_router.delete("/{id}")
async def delete_character(request: Request): 
    http_response = await request_adapter(request, character_delete_composer())
    return JSONResponse(content=http_response.body, status_code=http_response.status_code)
