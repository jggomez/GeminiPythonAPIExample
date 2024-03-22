from abc import ABC
from abc import abstractmethod
from typing import List

from ..domain import QuestionAnswers


class GeminiRepository(ABC):
    @abstractmethod
    async def get_questions(
        self,
        text: str,
        amount_question: int,
        complexity_question: str,
        language: str,
    ) -> List[QuestionAnswers]:
        pass
