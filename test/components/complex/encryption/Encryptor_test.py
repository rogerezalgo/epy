import re

import pytest

from app.components.complex.encryption import Encryption
from helpers import get_fake_txt_to_encrypt

__localizations = ['en', 'ru']
__texts = [(lambda locale: get_fake_txt_to_encrypt(locale))(locale) for locale in __localizations]
__invalid_chars = re.compile('[^A-Z0-9]')


@pytest.mark.parametrize('entry_text', __texts)
def test_encrypted_text_should_not_contain_invalid_chars(entry_text):
    encrypted = Encryption(entry_text)
    assert not re.findall(__invalid_chars, encrypted.encrypted_txt)


@pytest.mark.parametrize('entry_text', __texts)
def test_encryption_key_should_not_contain_invalid_chars(entry_text):
    encrypted = Encryption(entry_text)
    assert not re.findall(__invalid_chars, encrypted.key)
