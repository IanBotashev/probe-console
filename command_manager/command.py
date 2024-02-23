from command_manager.context import Context


class BaseCommand:
    """
    Representation for a command to be used by a command manager.
    """
    help_message = "Generic help message"
    alias = "base_command"
    required_args = 0

    @staticmethod
    def execute(_context: Context, args):
        """
        Execute this command
        :param _context: Context that this command will use
        :param args: Args, inputted as a list
        :return:
        """
        raise NotImplementedError("Command not implemented")


