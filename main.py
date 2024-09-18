from fastapi import FastAPI, Request
from utils import utils_functions
from dto import exercises_dtos
from typing import List

app = FastAPI()

@app.post("/max-in-list")
def exercise1(body: exercises_dtos.ListOfTen):
    return utils_functions.max_num(body.list)

@app.post("/max-prime-in-list")
def exercise2(body: exercises_dtos.ListOfTen):
    return utils_functions.max_prime_num(body.list)


