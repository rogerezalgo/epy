import pytest

from app.components.complex.decryption import Decryption
from app.components.complex.encryption import Encryption
from helpers.get_fake_txt_to_encrypt import get_fake_txt_to_encrypt

__localizations = ['en', 'ru']
__texts = [(lambda locale: get_fake_txt_to_encrypt(locale))(locale) for locale in __localizations]


@pytest.mark.parametrize('entry_text', __texts)
def test_should_decode_text_correctly(entry_text):
    encr = Encryption(entry_text)
    decr = Decryption(encr.encrypted_txt, encr.key)

    assert decr.original_txt == entry_text
