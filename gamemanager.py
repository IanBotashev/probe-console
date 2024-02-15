import threading
import time
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
