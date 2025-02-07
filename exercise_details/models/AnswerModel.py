from pydantic import BaseModel


class AnswerModel(BaseModel):
    answer: str
