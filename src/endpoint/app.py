from dotenv import load_dotenv
from fastapi import FastAPI

from . import questions_endpoint

load_dotenv()


def create_app():
    app = FastAPI()
    app.include_router(questions_endpoint.router)
    return app
