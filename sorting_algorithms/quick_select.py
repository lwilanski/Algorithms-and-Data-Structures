import random


def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def find_median(arr):
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) // 2)
    else:
        return 0.5 * (quickselect(arr, len(arr) // 2 - 1) + quickselect(arr, len(arr) // 2))
