# An exception that means a command errored "in-game", so we don't need to halt anything and just want to print this
class InGameException(Exception):
    pass