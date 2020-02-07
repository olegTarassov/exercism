import re


def response(hey_bob: str):

    question = re.compile("^.*[?]$")
    yell = re.compile("^[A-Z\\s,0-9]+[^a-zA-Z0-9]*[0-9A-Z,\\s]*[A-Z]+[!?0-9]*$")
    space = re.compile("\\s+")

    hey_bob = space.sub('', hey_bob)
    ans_q = question.search(hey_bob)
    ans_y = yell.search(hey_bob)

    if hey_bob == "":
        return "Fine. Be that way!"
    elif ans_q and ans_y:
        return "Calm down, I know what I'm doing!"
    elif ans_y:
        return "Whoa, chill out!"
    elif ans_q:
        return "Sure."
    else:
        return "Whatever."
    return question.search(hey_bob)


# Another approach
def response_2(hey_bob):
    hey_bob = hey_bob.strip()
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
