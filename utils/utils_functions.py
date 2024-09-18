from typing import List

def max_num(arr: List[int]):
    max = arr[0]
    pos = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            pos = i

    return {
        'max': max,
        'pos': pos
    }