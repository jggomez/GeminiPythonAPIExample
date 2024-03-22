from dataclasses import dataclass
from typing import Final
from typing import List

from PyPDF2 import PdfReader

from .domain import QuestionAnswers
from .repositories import GeminiRepository
from .use_case import UseCase

CLOUD_DOCS_DIRECTORY: Final = "docs"


@dataclass
class GetQuestionUseCaseParams:
    filename: str
    amount: int
    complexity: str
    language: str


class GetQuestionUseCase(UseCase):
    def __init__(
        self,
        gemini_repository: GeminiRepository,
        pdf_reader: PdfReader,
        bucket,
        local_storage_url: str,
    ) -> None:
        self.gemini_repository = gemini_repository
        self.pdf_reader = pdf_reader
        self.bucket = bucket
        self.local_storage_url = local_storage_url

    async def run(
        self, GetQuestionUseCaseParams: GetQuestionUseCaseParams
    ) -> List[QuestionAnswers]:
        local_file_path = self._download_file(GetQuestionUseCaseParams.filename)
        text = self._read_file(local_file_path)
        return await self.gemini_repository.get_questions(
            text=text,
            amount_question=GetQuestionUseCaseParams.amount,
            complexity_question=GetQuestionUseCaseParams.complexity,
            language=GetQuestionUseCaseParams.language,
        )

    def _download_file(self, name_file: str) -> str:
        file_path = f"{CLOUD_DOCS_DIRECTORY}/{name_file}"
        print("downloading file: ", file_path)
        blob = self.bucket.blob(file_path)
        file_name = f"{self.local_storage_url}/{blob.name.split('/')[1]}"
        print("local file path: ", file_name)
        blob.download_to_filename(file_name)
        return file_name

    def _read_file(self, path_file: str) -> str:
        print(f"reading file: {path_file}")
        text = ""
        with open(path_file, "rb") as pdf_file:
            reader = self.pdf_reader(pdf_file)
            for page in reader.pages:
                text += page.extract_text()
        return text
