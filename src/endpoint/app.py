from dotenv import load_dotenv
from fastapi import FastAPI

from . import questions_endpoint
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()


def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(questions_endpoint.router)
    return app
