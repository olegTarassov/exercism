def find_anagrams(word, candidates):

    sorted_word = ''.join(sorted(word))

    for num, can_word in enumerate(candidates):

        if ''.join(sorted(can_word)) == sorted_word:
            print("Words {}: {}".format(num, can_word))


ana_list = ["enlists", "google","inlets","banana"]

# inlets
find_anagrams("listen", ana_list)
