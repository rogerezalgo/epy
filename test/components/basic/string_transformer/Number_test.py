import pytest

from app.components.basic.string_transformer import Number
from helpers import generate_test_number_data


@pytest.mark.parametrize('int_number, representation, value', generate_test_number_data())
def test_should_translate_number_correctly(int_number: int, representation: int, value: str):
    num = Number(int_number)
    translated_number = num.translate_number_with_basis(representation)

    assert translated_number == value


@pytest.mark.parametrize('invalid_num', [-1])
def test_should_raise_value_error_if_constructor_got_invalid_parameter(invalid_num):
    with pytest.raises(ValueError):
        Number(invalid_num)


@pytest.mark.parametrize('invalid_scale', [1, 36])
def test_should_raise_value_error_if_translate_unexpected_number(invalid_scale):
    with pytest.raises(ValueError):
        Number(125846).translate_number_with_basis(invalid_scale)
