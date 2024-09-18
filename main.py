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

@app.get("/get-primes-between-100-300")
def exercise3():
    return utils_functions.getPrimesBetweenTwoNumbers(100, 300)

@app.post("/ended-numbers-in-4")
def exercise4(body: exercises_dtos.ListOfTen):
    arr: List[dict] = []

    for i in range(len(body.list)):
        if utils_functions.numberEndsIn4(body.list[i]):
            arr.append({
                "num": body.list[i],
                "pos": i
            })

    return  arr

@app.post("/repeated-max-number")
def exercise5(body: exercises_dtos.ListOfTen):
    response = utils_functions.max_num(body.list)

    rep = 0
    for i in range(len(body.list)):
        if response["max"] == body.list[i]:
            rep += 1

    return {
        "max": response["max"],
        "rep": rep
    }

@app.post("/avg-in-list")
def exercise6(body: exercises_dtos.ListOfTen):
    avg: int = round(utils_functions.avgList(body.list))

    for i in body.list:
        if i == avg:
            return {
                "avgInList": True,
                "avg": avg
            }

    return {
        "avgInList": False,
    }

@app.post("/sum-digits")
def exercise7(body: exercises_dtos.ListOfTen):
    max = 0
    pos = 0
    for i in range(len(body.list)):
        digitSum = utils_functions.sumDigits(body.list[i])
        if digitSum > max:
            max = digitSum
            pos = i

    return {
        "maxSumDigit": max,
        "pos": pos
    }