def is_armstrong_number(number):
    return sum( pow(int(x),len(str(number))) for x in str(number) ) == number
