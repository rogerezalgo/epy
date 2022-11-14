import random


def get_random_number(min_val: int, max_val: int):
    """
        Returns a random number in given interval not including max_val
    """

    return random.randrange(min_val, max_val, 1)
