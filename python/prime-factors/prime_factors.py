def factors(value: int) -> int:
    """
    return list of prime devisors
    """

    result = list()

    x = 2

    while x * x <= value:
        print(f"running {x}")
        if value % x:
            x += 1
        else:
            value = value // x
            result.append(x)

    if value > 1:
        result.append(value)

    return result
