from command_manager import Context
from command_manager.command import BaseCommand
from command_manager.commands.interface import interface_command_manager
from settings import MODULES
from objects.probe import Probe
import constants


def get_confirmation(prompt: str):
    """
    Asks a user a prompt and returns if they said yes or no to it.
    :param prompt: Prompt to ask
    :return: True if user says yes, False otherwise. Also returns what the user said as a secondary output
    """
    confirm = input(prompt).lower().strip()
    if confirm in ['y', 'yes']:
        return True, confirm

    else:
        return False, confirm


class ConsoleProbeInterfaceCommand(BaseCommand):
    help_message = "Interface with a probe."
    alias = "interface"
    required_args = 1

    @staticmethod
    def execute(context: Context, args):
        print("Attempting interface with probe...")
        probe = constants.player.get_probe(args[0])
        if not probe:
            print(f"Probe {args[0]} does not exist.")
            return

        interface_command_manager(probe)


class ConsoleListObjectsCommand(BaseCommand):
    help_message = "Lists all discovered objects in this system"
    alias = "objects"

    @staticmethod
    def execute(context: Context, args):
        print(f"{len(constants.game_manager.get_revealed_celestials())} known celestial(s):")
        for celestial in constants.game_manager.celestials:
            if celestial.revealed:
                print(f"  - {celestial}")


class ConsoleListProbesCommand(BaseCommand):
    help_message = "Lists all built probes"
    alias = "probes"

    @staticmethod
    def execute(context: Context, args):
        print(f"{len(constants.player.probes)} active probe(s):")
        for probe in constants.player.probes:
            print(f"  - {probe}")


class ConsoleStatusCommand(BaseCommand):
    help_message = "Displays the status our station"
    alias = "status"

    @staticmethod
    def execute(context: Context, args):
        print("Status:")
        print(f"  - Money: ${constants.player.money}")
        print(f"  - Active Probes: {len(constants.player.probes)}")


class ConsoleBuildProbeCommand(BaseCommand):
    help_message = "Design, build and launch a new probe"
    alias = "build"

    @staticmethod
    def execute(context: Context, args):
        # TODO: Allow user to build multiple of one module
        # TODO: Fix this super dirty code (somehow...?)
        # We essentially just ask the player a bunch of questions
        print("Initiating design interface...")
        print("Press Ctrl+C to cancel")
        try:
            name = input("Name of probe: ")

            included_modules = []
            for module in MODULES:
                confirm, response = get_confirmation(f"Install a {module.name}? (y/n)")
                if confirm:
                    included_modules.append(module)

            print(f"\nDesign blueprint for the {name} probe:")
            print("Modules:")
            for module in included_modules:
                print(f"  - {module.name}")
            print(f"Cost: {Probe.get_build_cost(included_modules)}")
            confirm = get_confirmation("Build? (y/n)")
            if not confirm:
                return
            constants.player.build_probe(name, included_modules)
            print("Probe has been built, now orbiting homeworld.")
        except KeyboardInterrupt:
            print("\nCancelling production...")