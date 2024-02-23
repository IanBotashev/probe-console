from command_manager.command import BaseCommand
from command_manager.context import Context
from pyparsing import Word, alphas, nums, OneOrMore, Optional, alphanums


class CommandManager:
    def __init__(self, commands, player, game_manager):
        self.commands = commands
        self.commands.append(HelpCommand)
        self.context = Context(player=player, game_manager=game_manager, command_manager=self)
        self.active = True

    def handle(self, raw_string):
        """
        Handle user input with this command manager and try to execute the command given
        :param raw_string: Full string that the user inputted
        :return: None
        """
        raw_string = raw_string.lower().strip()
        _command, args = self._parse_string(raw_string)

        for potential_command in self.commands:
            if _command == potential_command.alias:
                if potential_command.required_args != len(args):
                    print(f"Command '{potential_command.alias}' requires {potential_command.required_args} arguments, {len(args)} were given.")
                    return
                potential_command.execute(self.context, args)
                return

        print("Unknown command")

    def _parse_string(self, raw):
        """
        Parses a raw input string into something understandable
        :param raw:
        :return: command, args: List[]
        """
        _command = Word(alphas).setResultsName("command")  # Command must be alphabetic
        integer = Word(nums).setParseAction(lambda t: int(t[0]))  # Convert matched integers to Python ints
        string = Word(alphanums)  # Define what a 'string' argument looks like
        argument = integer | string  # An argument can be either an integer or a string
        parser = _command + Optional(OneOrMore(argument)).setResultsName("arguments")  # Command with optional arguments

        result = parser.parseString(raw)
        _command = result['command']
        arguments = [] if 'arguments' not in result.keys() else result['arguments']
        return _command, arguments


class HelpCommand(BaseCommand):
    help_message = "Shows this message"
    alias = "help"

    @staticmethod
    def execute(_context: Context, args):
        print("All available commands in the current context: ")
        for _command in _context.command_manager.commands:
            print(f"  - {_command.alias}: {_command.help_message}")
