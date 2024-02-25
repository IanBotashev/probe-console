import random

# Temporary, hopefully, keep these in here instead of messing with settings.py
PREFIXES = ['astro', 'lunar', 'solar', 'cosmo', 'galax', 'stellar']
SUFFIXES = ['eon', 'ara', 'ion', 'ius', 'ara', 'ona']
MYTH_NAMES = ['zeus', 'hera', 'apollo', 'athena', 'hermes', 'artemis', 'dionysus']

MIN_NUMBER = 1
MAX_NUMBER = 400


# TODO: Refine name generation
# Right now, we don't care for the type of the name we're generating.
def generate_name():
    """
    Generates a semi-plausible names for celestial objects
    :return: string
    """
    include_prefix = bool(random.getrandbits(1))
    include_suffix = bool(random.getrandbits(1))
    include_number = bool(random.getrandbits(1))
    result = random.choice(MYTH_NAMES)
    if include_prefix:
        result = random.choice(PREFIXES) + result

    if include_suffix:
        result += random.choice(SUFFIXES)

    if include_number:
        result += f"-{random.randint(MIN_NUMBER, MAX_NUMBER)}"

    return result


if __name__ == '__main__':
    for x in range(10):
        print(generate_name())