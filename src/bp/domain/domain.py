from dataclasses import dataclass


@dataclass
class QuestionAnswers:
    question: str
    answer: str
    options: list[str]
