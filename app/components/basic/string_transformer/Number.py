from string import ascii_lowercase, digits


class Number:
    """
        This class allows transforming some number to string with another scale of notation
        for given number
    """

    def __init__(self, n: int | str):
        self.number = int(n)

        if self.number < 0:
            raise ValueError(f'Parameter must be 0 or more')

    def translate_number_with_basis(self, basis: int) -> str:
        """
            This method translates number to another scale of notation by param {basis}
            and returns a string of the new number. Example it will return "b" if number = 11 and
            basis = 16. Another possible case: will return "100011" if number = 35 and basis = 2.
            And so on
        """

        if basis < 2 or basis > 35:
            raise ValueError(f'Expect the argument will be more than 1 and less than 36. But got {basis}')

        num_str: list[str] = list()
        is_number_transformed = False

        while not is_number_transformed:
            if self.number < basis:
                num_str.insert(0, self.__get_str_from_num(self.number))
                is_number_transformed = True
            else:
                num_str.insert(0, self.__get_str_from_num(self.number % basis))
                self.number = self.number // basis

        return ''.join(num_str)

    def __get_str_from_num(self, number: int) -> str:
        matches = digits + ascii_lowercase

        if matches[number]:
            return matches[number].upper()
        else:
            raise ValueError('Given number is not matching to some string')
