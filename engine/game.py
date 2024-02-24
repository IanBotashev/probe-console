from engine.tickmanager import TickManager
from engine.gamemanager import GameManager
from engine.player import Player
import shutil
from terminaltables import AsciiTable
from settings import ENABLE_INTRO
import constants


class Game:
    """
    Main class that runs the game.
    Initializes the tick and game manager.
    """
    def __init__(self):
        constants.tick_manager = TickManager()
        constants.game_manager = GameManager()
        constants.player = Player()
        self.running = False

    def run(self):
        """
        Entrypoint into the game. Sets everything into motion
        :return:
        """
        self.running = True

        if ENABLE_INTRO:
            self._intro()

        constants.tick_manager.start()
        constants.game_manager.start()
        constants.player.start()

    @staticmethod
    def _intro():
        """
        Displays the intro startup message
        :return:
        """
        intro_messages = [
            ["PROBEos (GNU/PROBE v1.5)"],
            [" * 0 available security updates"],
            ["Welcome, operator."],
            ["Type help for help."],
        ]
        table = AsciiTable(intro_messages)

        # Stretch table across entire terminal
        padding_spaces = shutil.get_terminal_size().columns - table.table_width + 1
        table.padding_right = padding_spaces

        print(table.table)
