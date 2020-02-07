import re

class Phone(object):

    PATTERN_VALID_NUMBER = re.compile(r"^1*[2-9][0-9]{2}[2-9][0-9]{2}[0-9]{4}$")
    PATTERN_TO_REMOVE = re.compile(r"[^0-9]")

    def __init__(self, phone_number):
        self.number = ''
        self.area_code = ''
        self.exchange_code = ''
        self.subscriber_number = ''

        clean_number = self._clean_number(phone_number)
        self._check_number(clean_number)
        self._parse_number(clean_number)

    def _clean_number(self, phone_number):
        return re.sub(self.PATTERN_TO_REMOVE, "", phone_number)

    def _check_number(self, phone_number):
        if not re.match(self.PATTERN_VALID_NUMBER, phone_number):
            raise ValueError('the phone number has not a valid format')

    def _parse_number(self, phone_number):
        self.number = phone_number[-10:]
        self.area_code = self.number[0:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[-4:]

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.subscriber_number}"