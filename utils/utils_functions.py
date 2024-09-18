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