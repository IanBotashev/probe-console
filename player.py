import shutil
from terminaltables import AsciiTable
from command_manager import CommandManager
from command_manager.commands.main_menu import MainMenuConnectCommand, MainMenuSystemCommand, MainMenuWorldsCommand
from command_manager.commands.console import *


class Player:
    """
    Handles the inputs from the player, essentially the connection between the game and the player.
    """
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.probes = []
        self.money = 100
        self.intro()

    def get_probe(self, probe_name: str):
        """
        Gets a probe from its name
        :param probe_name:  The name of the probe, string
        :return: Probe object or None
        """
        for probe in self.probes:
            if probe.name == probe_name:
                return probe

        return None

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

    def build_probe(self, name, modules):
        """
        'Builds' a probe and makes its location the homeworld.
        :param name: Name of the probe
        :param modules: Modules to include
        :return: Probe object
        """
        probe = Probe(name=name, modules=modules)
        probe.change_location(self.game_manager.capital_celestial, consume_fuel=False)
        self.probes.append(probe)
        return probe

    def main_menu(self):
        """
        Main menu, allows the player to start the world and what not.
        :return:
        """
        main_menu_cmd_manager = CommandManager(
            [MainMenuConnectCommand, MainMenuSystemCommand, MainMenuWorldsCommand],
            player=self,
            game_manager=self.game_manager)
        while not self.game_manager.running:
            cmd = input("main>")
            main_menu_cmd_manager.handle(cmd)

    def console(self):
        """
        Main loop for the console.
        When run, waits for the user to run a command, then handles it.
        :return:
        """
        console_cmd_manager = CommandManager(
            [ConsoleListObjectsCommand,
             ConsoleProbeInterfaceCommand,
             ConsoleListProbesCommand,
             ConsoleStatusCommand,
             ConsoleBuildProbeCommand],
            player=self,
            game_manager=self.game_manager)
        while console_cmd_manager.active and self.game_manager.running:
            cmd = input(">")
            console_cmd_manager.handle(cmd)
