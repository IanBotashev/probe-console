import random
import threading
import time
from objects.celestial import Celestial
from settings import TICK_SLEEP_TIME, RESOURCES, CELESTIAL_TYPES
from player import Player


class GameManager:
    """
    The Game Manager pulls the strings behind the scenes of the games.
    Responsibilities:
    - Run main game loop
    - Tick game time
    - Initialize player & console
    """
    def __init__(self):
        self.tick = 0
        self.running = False
        self.capital_celestial = Celestial("homeworld", CELESTIAL_TYPES[2], revealed=True, revealed_slots=True)
        self.celestials = self.generate_solar_systems()
        self.celestials.append(self.capital_celestial)
        self.player = Player(self)

    def main_loop(self):
        self.start_tick_system()
        self.player.console()

    def start_tick_system(self):
        """
        Starts the process for ticks by starting a thread running tick_system
        :return:
        """
        tick_thread = threading.Thread(target=self.next_tick)
        tick_thread.daemon = True  # Ensures the thread exits when the main program does
        tick_thread.start()

    def next_tick(self):
        """
        Ticks game time as specified in settings.py
        :return:
        """
        while self.running:
            time.sleep(TICK_SLEEP_TIME)
            self.tick += 1

    def generate_solar_systems(self):
        """
        Generates a random number of random celestials
        :return: Returns the list of random celestials
        """
        result = []
        for x in range(random.randint(5, 10)):
            new_celestial = Celestial.generate(CELESTIAL_TYPES, RESOURCES)
            result.append(new_celestial)

        return result

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
