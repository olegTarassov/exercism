def classify(number: int):
    sum = 0

    if number < 1:
        raise ValueError(number)

    for x in range(1, number):
        if number % x == 0:
            sum += x

    if sum == number:
        return "perfect"
    elif sum > number:
        return "abundant"
    elif sum < number:
        return "deficient"
    else:
        raise Exception("Not sure why this happened")
