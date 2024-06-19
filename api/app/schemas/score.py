from pydantic import BaseModel


class ScoreUpdate(BaseModel):
    username: str
