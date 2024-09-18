from typing import List

def max_num(arr: List[int]):
    maxInList = arr[0]
    pos = 0
    for i in range(len(arr)):
        if arr[i] > maxInList:
            maxInList = arr[i]
            pos = i

    return {
        'max': maxInList,
        'pos': pos
    }

def isPrime(num: int):
    if num < 1:
        return False

    band = True
    for i in range(2, num - 1):
        if num % i == 0:
            band = False
            break

    return band

def max_prime_num(arr: List[int]):
    maxInList = arr[0]
    pos = 0
    for i in range(len(arr)):
        if isPrime(arr[i]) and arr[i] > maxInList:
            maxInList = arr[i]
            pos = i

    return {
        'max': maxInList,
        'pos': pos
    }

def getPrimesBetweenTwoNumbers(num1: int, num2: int):
    arr: List[int] = []

    for i in range(num1, num2):
        if isPrime(i) and len(arr) < 10:
            arr.append(i)

    return arr

def numberEndsIn4(num: int):
    return num % 10 == 4

def avgList(arr: List[int]):
    sum = 0
    for i in arr:
        sum += i

    return sum / len(arr)

def sumDigits(num: int):
    strNum = str(num)
    sum = 0

    for i in strNum:
        sum += int(i)

    return sum

def factorial(num: int):
    fact = 1
    for i in range(num, 1, -1):
        fact *= i

    return fact
