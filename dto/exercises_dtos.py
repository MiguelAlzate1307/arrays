from pydantic import BaseModel, conlist

class ListOfTen(BaseModel):
    list: conlist(int, min_length=10, max_length=10)