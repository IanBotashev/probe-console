import random
from objects.celestial import Celestial
from settings import RESOURCES, CELESTIAL_TYPES
from engine.namegeneration import generate_name


class GameManager:
    """
    The Game Manager pulls the strings behind the scenes of the games.
    Responsibilities:
    - Run main game loop
    - Tick game time
    - Initialize player & console
    """
    def __init__(self):
        # In-game
        self.celestials = []
        self.capital_celestial = None

    def start(self):
        """
        Initialize solar system
        :return:
        """
        self.capital_celestial = Celestial("homeworld", CELESTIAL_TYPES[2], revealed=True, revealed_slots=True)
        self.celestials = self.generate_solar_systems()
        self.celestials.append(self.capital_celestial)

    def get_celestial_by_name(self, name, is_revealed=True):
        """
        Gets a celestial by its name
        :param name: Name to search for
        :param is_revealed: Whether or not the celestial must've been revealed (defaults to True)
        :return: Celestial object if found, otherwise None
        """
        for celestial in self.celestials:
            if celestial.name == name and celestial.revealed == is_revealed:
                return celestial

        return None

    def get_revealed_celestials(self):
        """
        :return: All revelealed celestials
        """
        return [celestial for celestial in self.celestials if celestial.revealed]

    @staticmethod
    def generate_celestial_name(existing):
        """
        Generates a random name for a celestial, and makes sure that name is not already taken
        :param existing: Celestials already generated
        :return: String of name
        """
        names = [obj.name for obj in existing]
        result = generate_name()
        while result in names:
            result = generate_name()

        return result

    @staticmethod
    def generate_solar_systems(number=random.randint(5, 10)):
        """
        Generates a random number of random celestials
        Attempts to generate names for them as well
        :param number: number of celestials to generate
        :return: Returns the list of random celestials
        """
        result = []
        for x in range(number):
            new_celestial = Celestial.generate(GameManager.generate_celestial_name(result), CELESTIAL_TYPES, RESOURCES)
            result.append(new_celestial)

        return result
