from Lib import random
from names import adjectives
from names import surnames


def get_random_name():
    name = adjectives.values[random.randrange(len(adjectives.values))] + "_" + surnames.values[random.randrange(len(surnames.values))]
    if name == "boring_wozniak":
        name = get_random_name()
    return name
