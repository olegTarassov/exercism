def sum_of_multiples(limit: int, multiples: list) -> int:
    multiple_result = set()

    for num in multiples:
        if num == 0:
            break
        multiple_result.update(range(num, limit, num))
    return sum(multiple_result)
