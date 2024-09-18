from pydantic import BaseModel, conlist

class Exercise1(BaseModel):
    list: conlist(int, min_length=10, max_length=10)