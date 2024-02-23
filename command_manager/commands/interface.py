# Commands that are for intefacing with probes
from command_manager import Context
from command_manager.command import BaseCommand
from command_manager import CommandManager


class InterfaceStatusCommand(BaseCommand):
    help_message = "Get status of this probe"
    alias = "status"

    @staticmethod
    def execute(_context: Context, args):
        print(_context.probe)


class InterfaceMoveCommand(BaseCommand):
    help_message = "Moves this probe to another location"
    alias = "move"
    required_args = 1

    @staticmethod
    def execute(_context: Context, args):
        location = _context.game_manager.get_celestial_by_name(args[0])
        if location is None:
            print(f"Could not find celestial named '{args[0]}'")

        _context.probe.change_location(location)
        print(f"Probe now orbiting {location.name}")


class InterfaceExitCommand(BaseCommand):
    help_message = "Disconnects the probe interface"
    alias = "exit"

    @staticmethod
    def execute(_context: Context, args):
        print("Disconnecting from probe...")
        _context.command_manager.active = False


def interface_command_manager(_context: Context, probe):
    """
    Runs the command manager when interfacing with a probe
    :param _context: Context object given to the initial command
    :param probe: Probe object that we are interfacing with
    :return:
    """
    probe_cmd_manager = CommandManager([InterfaceStatusCommand, InterfaceMoveCommand, InterfaceExitCommand], _context.player, _context.game_manager)
    probe_cmd_manager.context.add_kwarg("probe", probe)
    probe_cmd_manager.context.add_kwarg("command_manager", probe_cmd_manager)

    while probe_cmd_manager.active:
        cmd = input("probe>")
        probe_cmd_manager.handle(cmd)
