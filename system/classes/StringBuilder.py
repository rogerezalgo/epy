from system.constants import EMPTY_STRING


class StringBuilder:
    """
        Provides an interface to work with mutable sequence of strings
    """

    __text: list[str]

    def __init__(self, string=EMPTY_STRING):
        if not isinstance(string, str):
            raise ValueError('Parameter must be string')

        if not string:
            self.__text = list()
        else:
            self.__text = list(string)

    def to_str(self) -> str:
        """
            Returns a string representation of StringBuilder
        """

        return EMPTY_STRING.join(self.__text)

    def append(self, string: str) -> None:
        """
            Inserts param "string" at the end of the buffer
        """

        self.__text.append(string)

    def prepend(self, string: str) -> None:
        """
            Inserts param "string" at the start of the buffer
        """

        self.__text.insert(0, string)

    def shift(self) -> None:
        """
            Removes the first element from the buffer
        """

        self.__text.pop(0)

    def pop(self) -> None:
        """
            Removes the last element of the buffer
        """

        self.__text.pop()
