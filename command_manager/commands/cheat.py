# Debug commands
from command_manager import Context
from command_manager.command import BaseCommand
from settings import MODULES
import constants


class DiscoverAllCelestialsCheat(BaseCommand):
    help_message = "Discovers all celestials and their resources"
    alias = "cheatdiscoverall"

    @staticmethod
    def execute(context: Context, args):
        for celestial in constants.game_manager.celestials:
            celestial.revealed = True
            celestial.revealed_slots = True
        print("All celestials revealed")


class CreateTestProbeCheat(BaseCommand):
    help_message = "Creates a test probe."
    alias = "cheatprobe"

    @staticmethod
    def execute(context: Context, args):
        name = f"probe{len(constants.player.probes)}"
        constants.player.build_probe(name, MODULES)
        print(name)


class GetTickCheat(BaseCommand):
    help_message = "Prints current tick"
    alias = "tick"

    @staticmethod
    def execute(context: Context, args):
        print(constants.tick_manager.tick)
