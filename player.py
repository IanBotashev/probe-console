import os
import shutil

from terminaltables import AsciiTable


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
        while True:
            command = input("main>")
            command = command.lower().strip()
            if command == "help":
                print("Allowed commands:\n * system\n * worlds\n * connect {world}")
            elif command == "system":
                print("System Messages:\n  You have been assigned to a new world.\n  Please connect as soon as possible.")
            elif command == "worlds":
                print("Available worlds:\n * homeworld")
            elif command.startswith("connect"):
                if command == "connect homeworld":
                    print("Connecting...")
                    self.game_manager.running = True
                    print(" * Successfully connected\n\n")
                    break
                else:
                    print("Unknown world.")

    def console(self):
        """
        Main loop for the console.
        When run, waits for the user to run a command, then handles it.
        :return:
        """
        while self.game_manager.running:
            input(">")
