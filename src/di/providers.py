import os
from pathlib import Path
from typing import Final

import firebase_admin
import vertexai
from bp import GeminiRepository
from bp import GetQuestionUseCase
from bp import UseCase
from data import GeminiRepositoryImp
from fastapi import Depends
from firebase_admin import storage
from PyPDF2 import PdfReader
from vertexai.preview.generative_models import GenerationConfig
from vertexai.preview.generative_models import GenerativeModel

# Environment variable keys.
PROJECT_ID_KEY: Final = "PROJECT_ID"
LOCATION: Final = "us-central1"
MODEL_NAME_KEY: Final = "MODEL_NAME"
DEFAULT_MODEL: Final = "gemini-1.0-pro-001"
MAX_OUTPUT_TOKENS_DEFAULT: Final = 8182
MAX_OUTPUT_TOKENS_KEY: Final = "MAX_OUTPUT_TOKENS"
TEMP_KEY: Final = "TEMPERATURE"
TEMPERATURE_DEFAULT: Final = 0.0
RESOURCES_PATH: Final = Path("resources")
LOCAL_DOCS_DIRECTORY: Final = f"{RESOURCES_PATH}/docs"

firebase_admin.initialize_app(
    options={"storageBucket": "devhack-3f0c2.appspot.com"},
)


def get_generative_model_module() -> GenerativeModel:
    project_id = str(os.environ.get(PROJECT_ID_KEY))
    model = str(os.environ.get(MODEL_NAME_KEY, DEFAULT_MODEL))
    vertexai.init(project=project_id, location=LOCATION)
    return GenerativeModel(model)


def get_generation_config_module() -> GenerationConfig:
    max_output_tokens = int(
        os.environ.get(MAX_OUTPUT_TOKENS_KEY, MAX_OUTPUT_TOKENS_DEFAULT)
    )
    temperature = float(os.environ.get(TEMP_KEY, TEMPERATURE_DEFAULT))
    return GenerationConfig(
        temperature=temperature,
        max_output_tokens=max_output_tokens,
    )


def get_gemini_repository_module(
    get_generative_model_module: GenerativeModel = Depends(
        dependency=get_generative_model_module
    ),
    get_generation_config_module: GenerationConfig = Depends(
        dependency=get_generation_config_module
    ),
) -> GeminiRepository:
    return GeminiRepositoryImp(
        get_generative_model_module, get_generation_config_module
    )


def get_question_usecase_module(
    get_gemini_repository_module: GeminiRepository = Depends(
        dependency=get_gemini_repository_module
    ),
) -> UseCase:
    os.makedirs(LOCAL_DOCS_DIRECTORY, exist_ok=True)
    return GetQuestionUseCase(
        gemini_repository=get_gemini_repository_module,
        pdf_reader=PdfReader,
        bucket=storage.bucket(),
        local_storage_url=LOCAL_DOCS_DIRECTORY,
    )
