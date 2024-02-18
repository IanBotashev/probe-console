import shutil
from terminaltables import AsciiTable
from command_manager import CommandManager
from command_manager.commands.main_menu import MainMenuConnectCommand, MainMenuSystemCommand, MainMenuWorldsCommand


class Player:
    """
    Handles the inputs from the player, essentially the connection between the game and the player.
    """
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.intro()

    def intro(self):
        """
        Displays the intro startup message
        :return:
        """
        intro_messages = [
            ["PROBEos (GNU/PROBE v1.5)"],
            [" * 0 available security updates"],
            [" * 1 system message(s)"],
            [" * 1 world(s) assigned to you"],
            ["Welcome, operator."],
            ["Type help for help."],
        ]
        table = AsciiTable(intro_messages)

        # Stretch table across entire terminal
        padding_spaces = shutil.get_terminal_size().columns - table.table_width + 1
        table.padding_right = padding_spaces

        print(table.table)
        self.main_menu()

    def main_menu(self):
        """
        Main menu, allows the player to start the world and what not.
        :return:
        """
        main_menu_cmd_manager = CommandManager([MainMenuConnectCommand, MainMenuSystemCommand, MainMenuWorldsCommand], player=self, game_manager=self.game_manager)
        while not self.game_manager.running:
            cmd = input("main>")
            main_menu_cmd_manager.handle(cmd)

    def console(self):
        """
        Main loop for the console.
        When run, waits for the user to run a command, then handles it.
        :return:
        """
        console_cmd_manager = CommandManager([], player=self, game_manager=self.game_manager)
        while self.game_manager.running:
            cmd = input(">")
            console_cmd_manager.handle(cmd)
