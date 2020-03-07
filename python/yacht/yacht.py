"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.

ONES = (lambda x: 1 * x.count(1) )
TWOS = (lambda x: 2 * x.count(2) )
THREES = (lambda x: 3 * x.count(3) )
FOURS = (lambda x: 4 * x.count(4) )
FIVES = (lambda x: 5 * x.count(5) )
SIXES = (lambda x: 6 * x.count(6) )
FULL_HOUSE = (lambda x: sum(x) if sorted( countUniq(x).values() ) == [2,3] else 0)
FOUR_OF_A_KIND = (lambda x: four_of_a_kind( x ))
LITTLE_STRAIGHT = (lambda x: 30 if sorted(x) == [1,2,3,4,5] else 0)
BIG_STRAIGHT = (lambda x: 30 if sorted(x) == [2,3,4,5,6] else 0)
YACHT = (lambda x: 50 if len( set(x) ) == 1 else 0 )
CHOICE = sum


def countUniq( dice_list ):
    a = {}
    for x in dice_list:
        if x in a:
            a[x] += 1
        else:
            a[x] = 1
    return a


def four_of_a_kind( x ):
    group_counts = countUniq( x ).items()
    for x in group_counts:
        if x[1] >= 4:
            return x[0] * 4
        else:
            return 0


def score(dice, category):
    return category(dice)
