import pytest

from app.components.basic.string_transformer import String
from helpers.generate_test_number_data import generate_test_number_data


@pytest.mark.parametrize('number, notation_param, num_repr', generate_test_number_data())
def test_should_translate_number_from_string_representation(number: int, notation_param: int, num_repr: str):
    translated_number = String(num_repr).translate_num_to_decimal_using_notation(notation_param)

    assert number == translated_number


def test_should_raise_exception_if_invalid_number_representation():
    with pytest.raises(ValueError):
        String('blah-blah-blah').translate_num_to_decimal_using_notation(5)


def test_should_raise_exception_if_invalid_notation_scale():
    with pytest.raises(ValueError):
        String("").translate_num_to_decimal_using_notation(0)
