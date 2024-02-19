from command_manager import Context
from command_manager.command import BaseCommand
from command_manager.commands.interface import interface_command_manager


class ConsoleProbeInterfaceCommand(BaseCommand):
    help_message = "Interface with a probe."
    alias = "interface"

    @staticmethod
    def execute(_context: Context, args):
        if not args:
            print("No probe specified.")
            return

        print("Attempting interface with probe...")
        probe = _context.player.get_probe(args[0])
        if not probe:
            print(f"Probe {args[0]} does not exist.")
            return

        interface_command_manager(_context, probe)


class ConsoleObjectsCommandCommand(BaseCommand):
    help_message = "Lists all discovered objects in this system"
    alias = "objects"

    @staticmethod
    def execute(_context: Context, args):
        print("Known Celestials:")
        for celestial in _context.game_manager.celestials:
            if celestial.revealed:
                print(f"  - {celestial}")
