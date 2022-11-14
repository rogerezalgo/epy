from app.components.basic.db_provider import get_chars_from_db
from app.components.basic.string_transformer import Number
from helpers import get_random_number


class Encryption:
    def __init__(self, plain_text: str):
        self.__entry_text = plain_text

        self.__database: dict[str, str] = get_chars_from_db()
        self.__str_database: str = ''.join(self.__database.values())
        self.__encryption_key: list[int] = self.__get_encryption_key(len(self.__str_database))
        self.__translated_key: list[str] = self.__get_translated_collection(self.__encryption_key)
        self.__hashed_database: list[str] = self.__get_hashed_database(self.__str_database, self.__encryption_key)
        self.__encrypted_text: list[int] = self.__get_encrypted_text(self.__hashed_database, self.__entry_text)
        self.__translated_encrypted_text: list[str] = self.__get_translated_collection(self.__encrypted_text)

    @property
    def encrypted_txt(self) -> str:
        return self.__insert_spaces_and_get_full_str(self.__translated_encrypted_text)

    @property
    def key(self) -> str:
        return self.__insert_spaces_and_get_full_str(self.__translated_key)

    def __get_encryption_key(self, collection_length: int) -> list[int]:
        """
            Returns a random collection of unique numbers. This collection will be an encryption basis
        """
        random_collection_strings: set[str] = set()

        while len(random_collection_strings) != collection_length:
            # It has to convert to string to avoid sorted set
            random_collection_strings.add(f'{get_random_number(0, collection_length)}')

        return [(lambda num_str: int(num_str))(num_str) for num_str in random_collection_strings]

    def __get_translated_collection(self, number_collection: list[int]) -> list[str]:
        """
            Transforms numbers inside parameter collection to specific string with new number notation.
        """
        notation_scale = get_random_number(2, 36)

        translated_collection = [(lambda num: Number(num).translate_number_with_basis(notation_scale))
                                 (num) for num in number_collection]

        if len(f'{notation_scale}') == 1:
            translated_collection.insert(0, f'0{notation_scale}')
        else:
            translated_collection.insert(0, f'{notation_scale}')

        return translated_collection

    def __get_hashed_database(self, database_for_doing_hash: str, random_collection: list[int]) -> list[str]:
        """
            Takes a number from random_collection and appends into collection a letter, which located
            under same index (like this number) in database_for_doing_hash
        """

        return [(lambda idx: database_for_doing_hash[idx])
                (idx) for idx in random_collection]

    def __get_encrypted_text(self, hashed_database: list[str], text: str) -> list[int]:
        """
            Compares chars inside parameter "text" with chars inside hashed_database and adds to collection
            the index of match
        """

        return [(lambda char: hashed_database.index(char))(char) for char in text]

    def __define_spaces(self, start_index: int) -> str:
        """
            Takes English letters and numbers from database and joins them. Returns a slice of result string.
            This slice will be used like spaces to insert between encrypted chars
        """

        summary = self.__database['Numbers'] + self.__database['EnLower']

        return summary[start_index:len(summary)]

    def __insert_spaces_and_get_full_str(self, encrypted_collection: list[str]) -> str:
        """
            Inserts encrypted separates into collection from the parameter
        """
        enc_coll = list(encrypted_collection)
        notation_scale = enc_coll.pop(0)
        spaces = self.__define_spaces(int(notation_scale))

        outer_text_with_spaces = [notation_scale]  # Start with notation scale needs for decryption

        for ch in enc_coll:
            outer_text_with_spaces.append(ch + spaces[get_random_number(0, len(spaces))].upper())

        return ''.join(outer_text_with_spaces[:len(outer_text_with_spaces) - 1])
