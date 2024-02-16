class Context:
    """
    Contains variables that commands may use
    """
    def __init__(self, player, game_manager, command_manager):
        self.player = player
        self.game_manager = game_manager
        self.command_manager = command_manager
