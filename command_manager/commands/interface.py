# Commands that are for intefacing with probes
from command_manager import Context
from command_manager.command import BaseCommand
from command_manager import CommandManager


class InterfaceStatusCommand(BaseCommand):
    help_message = "Get status of this probe"
    alias = "status"

    @staticmethod
    def execute(context: Context, args):
        print(context.probe)


class InterfaceMoveCommand(BaseCommand):
    help_message = "Moves this probe to another location"
    alias = "move"
    required_args = 1

    @staticmethod
    def execute(context: Context, args):
        location = context.game_manager.get_celestial_by_name(args[0])
        if location is None:
            print(f"Could not find celestial named '{args[0]}'")
            return

        successful = context.probe.change_location(location)
        print(f"Probe now orbiting {location.name}")


class InterfaceListModulesCommand(BaseCommand):
    help_message = "Lists all the modules this probe has installed"
    alias = "modules"

    @staticmethod
    def execute(context: Context, args):
        for module in context.probe.modules:
            print(module)


def interface_command_manager(context: Context, probe):
    """
    Runs the command manager when interfacing with a probe
    :param context: Context object given to the initial command
    :param probe: Probe object that we are interfacing with
    :return:
    """
    probe_cmd_manager = CommandManager([InterfaceStatusCommand, InterfaceMoveCommand, InterfaceListModulesCommand], context.player, context.game_manager)
    probe_cmd_manager.context.add_kwarg("probe", probe)

    probe_cmd_manager.handle_loop(f"{probe.name}>", exit_message="Connection severed to probe.")
