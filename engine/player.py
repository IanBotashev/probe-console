from command_manager import CommandManager
from command_manager.commands.cheat import *
from command_manager.commands.console import *
from settings import ENABLE_CHEATS
import constants


class Player:
    """
    Handles the inputs from the player, essentially the connection between the game and the player.
    """
    def __init__(self):
        self.probes = []
        self.money = 100

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

    def add_money(self, amount):
        """
        Adds money to the player, negative or positive
        :param amount: Amount to tadd
        :return: None
        """
        self.money += amount

    def build_probe(self, name, modules):
        """
        'Builds' a probe and makes its location the homeworld.
        :param name: Name of the probe
        :param modules: Modules to include
        :return: Probe object
        """
        # TODO: Add a cost to building probes
        probe = Probe(name=name, modules=modules)
        probe.change_location(constants.game_manager.capital_celestial, consume_fuel=False)
        self.probes.append(probe)
        self.add_money(-Probe.get_build_cost(modules))
        return probe

    def start(self):
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
             ConsoleBuildProbeCommand])

        if ENABLE_CHEATS:
            console_cmd_manager.commands += [DiscoverAllCelestialsCheat, CreateTestProbeCheat, GetTickCheat]
        console_cmd_manager.handle_loop(">")

    def get_tick_objects(self):
        """
        Gets all the tick objects we have documented in this class
        :return:
        """
        return self.probes
