import json
from typing import List

from bp import GeminiRepository
from bp import QuestionAnswers
from vertexai.preview.generative_models import GenerationConfig
from vertexai.preview.generative_models import GenerativeModel


class GeminiRepositoryImp(GeminiRepository):
    def __init__(
        self, generative_model: GenerativeModel, generation_config: GenerationConfig
    ) -> None:
        self.generative_model = generative_model
        self.generation_config = generation_config

    async def get_questions(
        self,
        text: str,
        amount_question: int,
        complexity_question: str,
        language: str,
    ) -> List[QuestionAnswers]:
        print(
            f"amount_question: {amount_question}, complexity_question: {complexity_question}, language: {language}"
        )
        print(f"text: {text}")
        response = self.generative_model.generate_content(
            f"""
            You are an expert evaluator. You have the ability to understand an input document and generate questions based on its content.
            Generate a structured JSON object that contains {amount_question} questions based on the entire document. {complexity_question} questions for each chapter or section. Every question should have 5 options, only one option should be the correct.
            Generate all the questions based on the document context ONLY.
            The generated JSON structure array of objects should be as follows and:

                "question": "Which constellation is NOT part of the North Polar Sky?",
                "options": [
                    "Ursa Major",
                    "Orion",
                    "Ursa Minor",
                    "Cassiopeia",
                    "Draco"
                ],
                "answer": "Orion"

            Provide questions & answers for the following text:
            {text}

        """,
            generation_config=self.generation_config,
        )

        print(response)
        response_string = response.candidates[0].content.parts[0].text[7:-3]
        print(response_string)

        # validate and return exception
        questions_json = json.loads(response_string)

        questions = []

        for question in questions_json:
            questions.append(
                QuestionAnswers(
                    question=question["question"],
                    options=question["options"],
                    answer=question["answer"],
                )
            )

        return questions
