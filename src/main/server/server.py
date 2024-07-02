from fastapi import FastAPI
from src.main.routes.routes import character_router

app = FastAPI()

app.include_router(character_router)
