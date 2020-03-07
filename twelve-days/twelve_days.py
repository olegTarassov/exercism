def verse(x):
    numtoword = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
    }

        #"On the {} day of Christmas my true love gave to me: ",
    lyrics = [
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming",
    ]

    if x == 1:
        verses = lyrics[0].replace("and ", "")

    else:
        verses = ", ".join(lyrics[x-1::-1])

    return f"On the {numtoword[x]} day of Christmas my true love gave to me: {verses}"


def recite(start_verse, end_verse):
    if end_verse < 1 or end_verse > 12:
        raise Exception("Days out of Song Range: 1-12")

    return [verse(x) for x in range(start_verse, end_verse + 1)]
