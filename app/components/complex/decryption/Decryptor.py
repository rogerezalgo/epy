import re

from app.components.basic.db_provider import get_chars_from_db
from app.components.basic.string_transformer import String
from system.constants import EMPTY_STRING


class Decryption:
    def __init__(self, encrypted_txt: str, encryption_key: str):
        self.__encrypted_txt = encrypted_txt
        self.__encryption_key = encryption_key

        self.__encrypted_txt_common = self.__encrypted_txt[2:]
        self.__encryption_key_common = self.__encryption_key[2:]

        self.__notation_scale_of_encrypted_txt: int = int(self.__encrypted_txt[:2])
        self.__notation_scale_of_encryption_key: int = int(self.__encryption_key[:2])

        self.__database: dict[str, str] = get_chars_from_db()

        self.__encrypted_txt_without_spaces: list[str] = self.__remove_spaces(self.__encrypted_txt_common,
                                                                              self.__notation_scale_of_encrypted_txt)
        self.__encryption_key_without_spaces: list[str] = self.__remove_spaces(self.__encryption_key_common,
                                                                               self.__notation_scale_of_encryption_key)
        self.__encrypted_text_decimal: list[int] = \
            self.__transform_list_to_decimal_values(self.__encrypted_txt_without_spaces,
                                                    self.__notation_scale_of_encrypted_txt)
        self.__encryption_key_decimal: list[int] = \
            self.__transform_list_to_decimal_values(self.__encryption_key_without_spaces,
                                                    self.__notation_scale_of_encryption_key)
        self.__hashed_database: list[str] = self.__get_hashed_database(self.__database,
                                                                       self.__encryption_key_decimal)

    @property
    def original_txt(self) -> str:
        return self.__get_original_text(self.__encrypted_text_decimal, self.__hashed_database)

    def __define_spaces(self, notation_scale: int) -> str:
        """
            Returns the separates string for encrypted string with given notation scale
        """

        all_spaces = self.__database['Numbers'] + self.__database['EnLower']

        return all_spaces[notation_scale:].upper()

    def __remove_spaces(self, encrypted_txt: str, notation_scale: int) -> list[str]:
        """
            Removes all list items, over notation scale value
        """

        spaces = self.__define_spaces(notation_scale)

        return re.split(rf'[{spaces}]', encrypted_txt)

    def __transform_list_to_decimal_values(self, any_notation_scale_list: list[str], notation_scale: int) -> list[int]:
        """
            Takes a list which contains any notation scale numbers and transforms them to decimal numbers
        """

        return [(lambda str_num: String(str_num).translate_num_to_decimal_using_notation(notation_scale))
                (num) for num in any_notation_scale_list]

    def __get_hashed_database(self, database: dict[str, str], hash_key: list[int]) -> list[str]:
        """
            Takes hash key (the same encryption key) and on its basis makes the mixed database
            which was used for encryption
        """
        db: str = EMPTY_STRING.join(database.values())

        return [(lambda idx: db[idx])(idx) for idx in hash_key]

    def __get_original_text(self, text_decimal_chars: list[int], hashed_database: list[str]) -> str:
        """
            Repairs original text using hashed (or mixed) database
        """

        return EMPTY_STRING.join([(lambda idx: hashed_database[idx])(idx) for idx in text_decimal_chars])
