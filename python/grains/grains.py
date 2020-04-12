def square(number: int) -> int:

    if number < 1 or number > 64:
        raise ValueError("Negative number")

    # Readability + Speed
    total = 1
    for num in range(2, number+1):
        total = total * 2

    return total

    # return 2**(number-1)


def total() -> int:

    total = 0
    for tot in range(1, 65):
        total += square(tot)

    return total
