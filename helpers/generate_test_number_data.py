from pathlib import Path

import yaml

__data_file = Path.resolve(Path.cwd() / '../helpers/data/test_number.yml')


def generate_test_number_data() -> list[list[int, int, str]]:
    test_data = list()

    with open(__data_file, 'r') as file:
        data = yaml.safe_load(file)

    for rep in data['represents']:
        test_data.append([
            data['number'],
            int(rep),
            data['represents'][rep].upper()
        ])

    return test_data
