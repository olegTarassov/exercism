def recite(start_verse, end_verse):

    if end_verse < 1 or end_verse > 12:
        raise Exception("Days out of Song Range: 1-12")

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

    lyrics = [
        "On the {} day of Christmas my true love gave to me: ",
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

    song = list()

    for x in range(start_verse, end_verse + 1):
        if x == 1:
            song.append(lyrics[0].format(numtoword[x]) + lyrics[1].replace("and ", ""))

        else:
            song.append(
                lyrics[0].format(numtoword[x])
                + ", ".join(lyrics[line] for line in range(x, 0, -1))
            )

    return song
