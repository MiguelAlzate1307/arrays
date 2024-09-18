from fastapi import FastAPI, Request
from utils import utils_functions
from dto import exercises_dtos
from typing import List

app = FastAPI()

@app.post("/exercise-1")
async def exercise1(body: exercises_dtos.Exercise1):
    return utils_functions.max_num(body.list)

