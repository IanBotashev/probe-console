import threading
import time
from engine.event import Event
from settings import TICK_SLEEP_TIME
import constants  # Needs to be like this in here, for some reason.


class TickManager:
    """
    Keeps track of ticks
    """
    def __init__(self):
        self.tick = 0
        self.tick_event = Event()

    def start(self):
        """
        Starts the process for ticks by starting a thread
        :return: None
        """
        tick_thread = threading.Thread(target=self.next)
        tick_thread.daemon = True  # Ensures the thread exits when the main program does
        tick_thread.start()

    def next(self):
        """
        Ticks game time as specified in settings.py
        :return: None
        """
        while constants.game.running:
            # Run a tick event at 0, instead of waiting for 1.
            self.tick_event.trigger(tick=self.tick)
            time.sleep(TICK_SLEEP_TIME)
            self.tick += 1
