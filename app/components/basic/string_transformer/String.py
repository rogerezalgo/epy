from string import ascii_uppercase, digits


class String:
    """
        This class allows transforming some non-decimal number to decimal
    """

    def __init__(self, num_str: str):
        self.__number = num_str

        self.__matches: str = f'{digits + ascii_uppercase}'

    def translate_num_to_decimal_using_notation(self, notation_scale: int) -> int:
        """
            Returns decimal number for letter representation
        """

        if notation_scale < 2 or notation_scale >= 36:
            raise ValueError('Notation scale must be more than 1 and less than 36')

        reversed_decimal_number: list[int] = [(lambda n: self.__get_num_from_str(n))(n)
                                              for n in self.__number][::-1]
        result = 0

        for n in range(len(reversed_decimal_number)):
            current = reversed_decimal_number[n]
            result += current * (notation_scale ** reversed_decimal_number.index(current))
            reversed_decimal_number[n] = 0

        return result

    def __get_num_from_str(self, num_str: str) -> int:
        if num_str in self.__matches:
            return self.__matches.index(num_str)
        else:
            raise ValueError('Given string is not of any number representation')
