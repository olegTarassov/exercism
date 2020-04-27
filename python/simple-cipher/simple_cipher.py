import string
import secrets


class Cipher:
    def __init__(self, key=None):
        self.alphabet = string.ascii_lowercase

        if not key:
            self.key = "".join(secrets.choice(self.alphabet) for i in range(100))
        else:
            self.key = key

    def __key_numeric(self, index: int) -> str:
        """
        Return numerical value for key
        """
        return self.alphabet.index(self.key[index % len(self.key)])

    def __alpha_numeric(self, index: str) -> str:
        """
        Return numerical value for letter
        """
        return self.alphabet.index(index)

    def __alpha_char(self, index: int) -> str:
        """
        Convert numerical value to its respectable letter
        """
        return self.alphabet[index % len(self.alphabet)]

    def encode(self, text: str) -> str:
        """
        Encrypt string using cipher key
        """

        return "".join(
            [
                self.__alpha_char(
                    self.__alpha_numeric(letter) + self.__key_numeric(index)
                )
                for index, letter in enumerate(text)
            ]
        )

    def decode(self, text):
        """
        Decrypt string using cipher key
        """

        return "".join(
            [
                self.__alpha_char(
                    self.__alpha_numeric(letter) - self.__key_numeric(index)
                )
                for index, letter in enumerate(text)
            ]
        )

    def encode_clean(self, text: str) -> str:
        """
        Encrypt string using cipher key
        A non pythonic approach but more readable
        """

        result = ""
        for index, letter in enumerate(text):
            # Get key weigthed value
            key_value = self.__key_numeric(index)

            # Get letter weighted value
            letter_value = self.__alpha_numeric(letter)

            # Add key to character tp encode
            result += self.__alpha_char(letter_value + key_value)
        return result
