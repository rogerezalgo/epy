from faker import Faker


def get_fake_txt_to_encrypt(locale: str) -> str:
    output = list()

    if locale == 'ru':
        for _ in range(10):
            output.append(Faker('ru_RU').text())
    elif locale == 'en':
        for _ in range(10):
            output.append(Faker('en_US').text())

    return ''.join(output)
