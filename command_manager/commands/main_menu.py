from command_manager import Context
from command_manager.command import BaseCommand


class MainMenuSystemCommand(BaseCommand):
    help_message = "Shows unread system messages"
    alias = "system"

    @staticmethod
    def execute(context: Context, args):
        print("System Messages:\n  You have been assigned to a new world.\n  Please connect as soon as possible.")


class MainMenuWorldsCommand(BaseCommand):
    help_message = "Shows assigned worlds"
    alias = "worlds"

    @staticmethod
    def execute(context: Context, args):
        print("Available worlds:\n * homeworld")


class MainMenuConnectCommand(BaseCommand):
    help_message = "Connects to an assigned world"
    alias = "connect"
    required_args = 1

    @staticmethod
    def execute(context: Context, args):
        if args[0] == "homeworld":
            print("Connecting...")
            context.game_manager.running = True
            context.command_manager.active = False
            print(" * Successfully connected.\n\n")
        else:
            print("Unknown world.")
