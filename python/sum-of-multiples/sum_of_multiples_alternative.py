def sum_of_multiples(limit: int, multiples: list) -> int:
    return sum({
        x
        for multiple in multiples
        for x in range(multiple, limit, multiple)
    })
