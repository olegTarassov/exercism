import math


def triplets_with_sum(number:int)->list:
    """
    a < b < c
    a^2 + b^2 = c^2
    """
    result = list()

    for b in range(number):
        for a in range(1,b):
            c = math.sqrt(a**2 + b**2)

            if c % 1 == 0 and (a + b + c) == number:
                result.append([a, b, int(c)])
    return result


def triplets_in_range(start: int, end: int)-> list:

    result = list()

    for b in range(start, end):
        for a in range(start,b):
            c = math.sqrt(a**2 + b**2)

            if c % 1 == 0:
                result.append([a, b, int(c)])
    return result


def is_triplet(triplet: list)-> bool:
    return True if triplet[0]**2 + triplet[1]**2 == triplet[2]**2 else False
