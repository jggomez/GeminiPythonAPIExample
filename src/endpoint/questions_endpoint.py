from typing import Final
from typing import List

from bp import GetQuestionUseCase
from bp import GetQuestionUseCaseParams
from di import providers
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from pydantic import BaseModel


router = APIRouter()

CODE: Final = "code"
MESSAGE: Final = "message"


class RequestBody(BaseModel):
    filename: str
    amount: int
    complexity: str
    language: str


class QuestionsResponse(BaseModel):
    question: str
    options: List[str]
    answer: str


@router.post("/apis/v1/questions", name="Create Q&A")
async def create_create_answers(
    request_body: RequestBody,
    response: Response,
    create_dynamic_pathway_use_case: GetQuestionUseCase = Depends(
        providers.get_question_usecase_module
    ),
):
    try:
        questions = await create_dynamic_pathway_use_case.run(
            GetQuestionUseCaseParams(
                filename=request_body.filename,
                amount=request_body.amount,
                complexity=request_body.complexity,
                language=request_body.language,
            )
        )

        questions_response = [
            QuestionsResponse(
                question=question.question,
                options=question.options,
                answer=question.answer,
            )
            for question in questions
        ]

        response.status_code = status.HTTP_200_OK
        return questions_response

    except Exception as error:
        print("Error in create_create_answers: ", error)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {CODE: 500, MESSAGE: str(error)}
