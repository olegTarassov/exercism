import re


def is_valid(isbn: str) -> bool:
    """is multiplied by its (integer) weight, descending from 10 to 2, and the sum of these nine products found
    """
    number_pattern = re.compile(r"^\d{1}-?\d{3}-?\d{5}-?[0-8|X]$")

    if not number_pattern.search(isbn.strip()):
        return False

    new_isbn = list(isbn.strip().replace('-', ''))

    if new_isbn[-1] == 'X':
        new_isbn[-1] = '10'

    clean_isbn = map(int, new_isbn)

    return sum(factors[0] * factors[1] for factors in zip(clean_isbn, range(10, 0, -1))) % 11 == 0
