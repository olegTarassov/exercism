import random, string


class Robot(object):
    def __init__(self):
        random.seed()
        self.reset()

    def reset(self):
    # factory settings, name gets wiped. Result produced such as RX837 or BC811
        self.name = ''.join(random.sample(string.ascii_uppercase, k=2) + random.sample(string.digits, k=3))
