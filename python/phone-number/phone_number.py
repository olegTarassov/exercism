
class Phone(object):
    def __init__(self, phone_number):
        self.number = self.__removeNonDigit( phone_number )

        self.number = self.__removeCountryCode( self.number )

        self.area_code = self.__getAreaCode( self.number )

        self.exchange_code = self.__getexchangeCode( self.number )

    def pretty(self):
        """
        return phone number pretty format
        """
        return "(" + self.area_code + ")" + " " + self.exchange_code + "-" + self.number[-4:]


    def __removeNonDigit( self, num ):
        """
        Accepts a list and returns valid String
        """

        tempNumber = ''.join([ x for x in num if x.isdigit() ])

        # Valid if contains (CountryCode + AreaCode or AreaCode) + PhoneNumber
        if len( tempNumber ) != 11 and len( tempNumber ) != 10:
            raise ValueError("Invalid Phone Number Length, got:", len(tempNumber))

        return tempNumber

    def __removeCountryCode(self, num):
        """
        Trims US/CAN Country Code
        """

        # Valid only for Country Code 1
        if len( num ) == 11 and num[0] != "1":
            raise ValueError("Invalid Country Code, can only be 1, got :", num[0])
        elif len( num ) == 11 and num[0] == "1":
            return num[1:]
        else:
            return num

    def __getAreaCode( self, num ):
        """
        returns 3 digit Area Code
        """

        if num[0] == "0" or num[0] == "1":
            raise ValueError("Invalid Area Code, cannot be:", num[0])

        return num[0:3]

    def __getexchangeCode( self, num ):
        """
        return 3 digit exchange code
        """

        if num[3] == "0" or num[3] == "1":
            raise ValueError("Invalid Exchange Code, cannot be:", num[3])

        return num[3:6]
