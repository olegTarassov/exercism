def find_anagrams(word, candidates):

    sorted_word = sorted(word.lower())

    return [
        can_word
        for can_word in candidates
        if sorted(can_word.lower()) == sorted_word
        and can_word.lower() != word.lower()
    ]
