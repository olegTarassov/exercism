def convert(number: int) -> str:
    sound = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

    tmp_return = ''.join(v for k, v in sound if number % k == 0)

    return tmp_return or str(number)
