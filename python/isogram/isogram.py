import re


def is_isogram(word: str) -> str:
    """
    Clean word to CHAR only before valdiation.
    """
    pattern = re.compile('[\W]+')
    clean_word = pattern.sub('', word).lower()

    return len(clean_word) == len(set(clean_word))
