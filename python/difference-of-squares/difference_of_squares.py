def square_of_sum(number: int) -> int:
    """
    (1 + 2 + ... + 10)² = 55² = 3025
    """
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """
    1² + 2² + ... + 10² = 385.
    """
    return sum(x ** 2 for x in range(1, number + 1))


def difference_of_squares(number: int) -> int:
    """
    Square of Sum - Sum of Squares
    """
    return square_of_sum(number) - sum_of_squares(number)
