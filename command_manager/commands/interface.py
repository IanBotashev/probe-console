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


def interface_command_manager(_context: Context, probe):
    """
    Runs the command manager when interfacing with a probe
    :param _context: Context object given to the initial command
    :param probe: Probe object that we are interfacing with
    :return:
    """
    probe_cmd_manager = CommandManager([InterfaceStatusCommand], _context.player, _context.game_manager)
    probe_cmd_manager.context.add_kwarg("probe", probe)

    while probe_cmd_manager.active:
        cmd = input("probe>")
        probe_cmd_manager.handle(cmd)
