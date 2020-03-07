import string

def is_pangram(sentence):
    alpha_list = list(string.ascii_lowercase)
    sentence_test = sentence.lower()

    # Iterate each alphabet character over string
    for letter in alpha_list:
      if letter not in sentence_test:
        return (False)

    # Matched all Alphabet characters at least once
    return True


from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram_good(string):
    return ALPHABET.issubset(string.lower())

def is_pangram_pythonic(sentence):
    return all(letter in sentence.lower() for letter in ascii_lowercase)


test="the quick brown fox jumps over the lazy dog"

print(is_pangram_pythonic(test))