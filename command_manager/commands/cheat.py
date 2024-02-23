# Debug commands
from command_manager import Context
from command_manager.command import BaseCommand
from settings import MODULES
from objects.probe import Probe


class DiscoverAllCelestialsCheat(BaseCommand):
    help_message = "Discovers all celestials and their resources"
    alias = "cheatdiscoverall"

    @staticmethod
    def execute(context: Context, args):
        for celestial in context.game_manager.celestials:
            celestial.revealed = True
            celestial.revealed_slots = True
        print("All celestials revealed")


class CreateTestProbeCheat(BaseCommand):
    help_message = "Creates a test probe."
    alias = "cheatprobe"

    @staticmethod
    def execute(context: Context, args):
        name = f"probe{len(context.player.probes)}"
        context.player.build_probe(name, MODULES)
        print(name)


class GetTickCheat(BaseCommand):
    help_message = "Prints current tick"
    alias = "tick"

    @staticmethod
    def execute(context: Context, args):
        print(context.game_manager.tick)
