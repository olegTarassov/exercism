def find_anagrams(word, candidates):

    sorted_word = "".join(sorted(word.lower()))

    return [
        can_word
        for can_word in candidates
        if "".join(sorted(can_word.lower())) == sorted_word
        and can_word.lower() != word.lower()
    ]
