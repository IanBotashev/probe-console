from command_manager.command import BaseCommand
from command_manager.context import Context
from pyparsing import Word, nums, OneOrMore, Optional, printables
from engine.exceptions import InGameException


class CommandManager:
    def __init__(self, commands):
        self.commands = commands
        self.commands.append(HelpCommand)
        self.context = Context(command_manager=self)
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
                    raise InGameException(f"Command '{potential_command.alias}' requires {potential_command.required_args} arguments, {len(args)} were given.")
                potential_command.execute(self.context, args)
                return

        print("Unknown command")

    def handle_loop(self, prompt: str, exit_message="exiting..."):
        """
        Optional loop to take user input and then handle it internally.
        Allows for handling of KeyboardInterrupts automatically to ONLY close down THIS cmd manager.
        Can be done normally, but simplifies it.
        Provides an optional exit message to print out when an interrupt is received
        :param prompt: Prompt to ask the user each time for input
        :param exit_message: Optional exit message to print when interrupted
        :return: None
        """
        while self.active:
            try:
                command = input(prompt)
                self.handle(command)
            except KeyboardInterrupt:
                self.active = False
                if exit_message is not None:
                    # Make sure we don't intersect with other lines
                    print("\n" + exit_message)

            except InGameException as e:
                # We've caught an exception that only has meaning to the player, not us.
                # Just print it and move on.
                print(e)

    @staticmethod
    def _parse_string(raw):
        """
        Parses a raw input string into something understandable
        :param raw:
        :return: command, args: List[]
        """
        # TODO: Fix issue where just pressing enter raises an exception
        # pyparsing.exceptions.ParseException: Expected W:(!-~)  (at char 0), (line:1, col:1)
        printables_without_space = printables.replace(" ", "")
        _command = Word(printables_without_space).setResultsName("command")  # Command must be alphabetic
        integer = Word(nums).setParseAction(lambda t: int(t[0]))  # Convert matched integers to Python ints
        string = Word(printables_without_space)  # Define what a 'string' argument looks like
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
    def execute(context: Context, args):
        print("All available commands in this context: ")
        for _command in context.command_manager.commands:
            print(f"  - {_command.alias}: {_command.help_message}")
